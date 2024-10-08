import os
import yaml

data_dict = {0: "0炉子开关.txt", 1: "1炉丝电机.txt", 2: "2转机1.txt", 3: "3样提机2.txt", 4: "4炉上机3.txt",
             5: "5炉中机4.txt", 6: "6炉下机5.txt", 7: "7电机状态查询.txt", 8: "8磁场.txt", 9: "9电机磁场电流.txt",
             "A": "A炉丝加热电压.txt", "B": "BPID控温曲线.txt", "C": "C在线监控状态查询.txt", "D": "D电机关闭设置.txt",
             "E": "E在线监控表头设置.txt", "F": "FPID参数设置动作表.txt"}
conf_dict = {0: "FurnaceSwitch.yaml", 1: "HearthWireMotor.yaml", 2: "Transfer1.yaml", 3: "Sample2.yaml",
             4: "Stove3.yaml", 5: "Stove4.yaml", 6: "Stove5.yaml", 7: "MotorStatusInquiry.yaml", 8: "MagneticField.yaml",
             9: "MotorMagneticFieldCurrent.yaml", "A": "FurnaceWireHeating.yaml", "B": "PIDTemperatureControl.yaml",
             "C": "OnlineMonitoringStatus.yaml", "D": "MotorClosing.yaml"}

base_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")
data_file_path = base_path + "\\data\\"
config_file_path = base_path + "\\config\\"


# 存储数据到文件
def store_data(hex_data, action_code):
    """
    保存16进制的动作编码到txt文件

    :param hex_data: 要存储的16进制数据
    :param action_code: 动作类别的标识（总共16个动作）
    :return:
    """
    # 写入文件路径
    file_path = os.path.join(data_file_path, data_dict[action_code])
    # 打开文件并写入数据
    with open(file_path, 'a') as file:
        file.write(hex_data + '\n')


# 获取动作配置参数信息
def get_config(action_code):
    """
    获取动作配置参数信息（不同设置对应的16进制值）
    :param action_code: 动作类别编码
    :return: action_code动作类别对应的参数配置信息
    """
    conf_path = os.path.join(config_file_path, conf_dict[action_code])
    with open(conf_path, 'r', encoding='utf-8') as file:
        conf = yaml.safe_load(file)
    return conf


def get_action_id(config_hex, action_code):
    """
    根据配置参数编码查询动作ID，若存在则返回已存在的ID，不存在递增生成一个新ID返回
    :param config_hex:
    :param action_code:
    :return: 返回一个Tuple，(动作id, 是否是新动作：是 = 1，否 = 0)
    """
    config_hex = str(config_hex).upper()
    final_id = str(action_code) + "000"
    # 读取文件
    # data_file = QFile(":/data/" + data_dict[action_code])
    # data_file.open(QIODevice.ReadOnly | QIODevice.Text)
    # all_data = str(data_file.readAll(), encoding='utf-8')
    with open(data_file_path + data_dict[action_code], 'r', encoding='utf-8') as data_file:
        all_data = data_file.read()

    # 为空直接返回
    if len(all_data) == 0:
        return final_id, 1

    list_all = all_data.split("\n")
    print(">>>>>>开始比对配置生成动作ID>>>>>")
    for line in list_all:
        # 读取到空行跳过
        if line == '':
            continue
        action_id, config = tuple(line.split(" "))
        final_id = action_id
        # 找到相同的参数配置则返回相同的ID
        print(f"比对:\n>>{config}\n>>{config_hex}")
        if config_hex == config:
            data_file.close()
            print(f">>>>>>比对结束，生成的动作ID为：{final_id}，是否为新ID：否>>>>>")
            return final_id, 0
    data_file.close()
    # 没找到相同的ID, 在最后一个ID号的基础上+1
    final_id = format(int(final_id, 16) + 1, '04X')
    print(f">>>>>>比对结束，生成的动作ID为：{final_id}，是否为新ID：是>>>>>")
    return final_id, 1


def get_action_id_pid_temp_control(config_hex, action_code):
    """
    PID温度控制动作ID生成规则: 根据配置参数编码查询动作ID，若存在则返回已存在的ID，不存在递增生成一个新ID返回
    :param config_hex: 配置参数编码
    :param action_code: 动作代码
    :return: 返回一个Tuple，(动作id, 是否是新动作：是 = 1，否 = 0)
    """
    config_hex = str(config_hex).upper()  # 配置参数编码转换为大写
    final_id = str(action_code) + "000"  # 初始动作ID

    # 读取文件内容
    try:
        with open(data_file_path + data_dict[action_code], 'r', encoding='utf-8') as data_file:
            all_data = data_file.read()
    except FileNotFoundError:
        print(f"文件未找到：{data_file_path + data_dict[action_code]}")
        return final_id, 1

    # 如果文件为空，直接返回初始ID
    if len(all_data) == 0:
        return final_id, 1

    list_all = all_data.strip().split("\n")
    print(">>>>>>开始比对配置生成动作ID>>>>>")

    for line in list_all:
        if line.strip() == '':  # 跳过空行
            continue
        action_id, config = tuple(line.split(" "))
        final_id = action_id  # 获取文件中的最后一个ID

        # 特殊情况：config_hex 的前四个字符为 "0000"，只对比前四个字符
        if config_hex[:4] == "0000":
            print(f"特殊情况比对前四个字符:\n>>{config[:4]}\n>>{config_hex[:4]}")
            if config[:4] == config_hex[:4]:
                print(f">>>>>>比对结束，生成的动作ID为：{final_id}，是否为新ID：否>>>>>")
                return final_id, 0
        else:
            # 正常情况下比对整个 config_hex
            print(f"比对:\n>>{config}\n>>{config_hex}")
            if config_hex == config:
                print(f">>>>>>比对结束，生成的动作ID为：{final_id}，是否为新ID：否>>>>>")
                return final_id, 0

    # 没有找到匹配的配置参数，生成新的动作ID
    final_id = format(int(final_id, 16) + 1, '04X')
    print(f">>>>>>比对结束，生成的动作ID为：{final_id}，是否为新ID：是>>>>>")
    return final_id, 1


def hex_string_to_binary_file(hex_string, output_file_path):
    print("++++++准备写入文件：", hex_string)
    # 将十六进制字符串转换为字节对象
    hex_bytes = bytes.fromhex(hex_string)
    # 将字节写入二进制文件
    with open(output_file_path, 'wb') as binary_file:
        binary_file.write(hex_bytes)
    print("++++++写入完成：", hex_string)


def load_action_bin_to_data(action_bin_file_folder):
    # 获取文件夹中所有文件的列表
    file_list = os.listdir(action_bin_file_folder)
    # 筛选出文件名带有 '.bin' 的文件
    bin_files = [file for file in file_list if file.endswith('.bin') and file.startswith("AT")]
    # 遍历所有文件
    for bin_file in bin_files:
        bin_file_path = action_bin_file_folder + bin_file
        with open(bin_file_path, "rb") as file:
            # 读取文件内容
            binary_data = file.read()
            # 将二进制数据转换为十六进制字符串
            hex_representation = binary_data.hex().upper()
            # 动作ID
            action_id = hex_representation[2:4] + hex_representation[0:2]
            # 参数编码
            config_code = hex_representation[4:]
            # 打印输出
            print(f"{action_id} -> {config_code}")
            # 保存到.txt文件
            action_code = action_id[0:1]
            if action_code.isdigit():
                action_code = int(action_code)
            store_data(action_id + " " + config_code, action_code)


def clear_data():
    """
    清空data文件夹下的数据
    :return:
    """
    file_list = os.listdir(data_file_path)
    for file_name in file_list:
        bin_file_path = data_file_path + file_name
        with open(bin_file_path, "w") as file:
            file.write("")


if __name__ == "__main__":
    # 示例用法
    # hex_string = "2400F0C33300190033001a0083001b000F00FA00CC000201"
    # output_file_path = "output.bin"
    # hex_string_to_binary_file(hex_string, output_file_path)
    # clear_data()
    # load_action_bin_to_data("S:\\project\\高温柜\\20230828高温流程\\0828\\动作表\\")
    print(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".."))
