import os
import re
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.totaltable import Ui_TotalTable
from utils.data_utils import get_config, hex_string_to_binary_file
from tkinter import Tk, filedialog


class TotalTableDlg(QDialog, Ui_TotalTable):
    def __init__(self):
        super(TotalTableDlg, self).__init__()
        self.setupUi(self)
        # 静态表长度
        self.static_length = 0
        # 静态表的十六进制值
        self.static_val_hex = ''
        # 静态表内容
        self.static_content_hex = ''
        # 动作表长度
        self.action_length = 0
        # 动作表的十六进制值
        self.action_val_hex = ''
        # 动作表内容
        self.action_content_hex = ''
        # 动态表长度
        self.dynamic_length = 0
        # 动态表的十六进制值
        self.dynamic_val_hex = ''
        # 动态表内容
        self.dynamic_content_hex = ''
        # 监控表长度
        self.monitoring_length = 0
        # 监控表的十六进制值
        self.monitoring_val_hex = ''
        # 监控表内容
        self.monitoring_content_hex = ''
        # 总表长度
        self.total_table_length = 0
        # 总表的十六进制值
        self.total_table_length_val_hex = ''
        # 总表配置值
        self.total_table_config = '00F0'
        # 电机的参数配置值
        self.motor_hex_str = ''
        # 表头的十六进制参数值
        self.table_head_hex = ''
        # 总表的十六进制参数值
        self.total_table_hex = ''
        # 表头+3总表(3次总表)的十六进制配置值
        self.finally_total_table_hex = ''
        # 读取配置
        furnace_config = get_config('E')
        # ------------电机选择--------------
        self.motor1_val = furnace_config["motor_select"]["motor_1"]
        self.motor2_val = furnace_config["motor_select"]["motor_2"]
        self.motor3_val = furnace_config["motor_select"]["motor_3"]
        self.motor4_val = furnace_config["motor_select"]["motor_4"]
        self.motor5_val = furnace_config["motor_select"]["motor_5"]
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 电机复选框状态改变
        self.motor_1.stateChanged.connect(self.motor1_state_changed)
        self.motor_2.stateChanged.connect(self.motor2_state_changed)
        self.motor_3.stateChanged.connect(self.motor3_state_changed)
        self.motor_4.stateChanged.connect(self.motor4_state_changed)
        self.motor_5.stateChanged.connect(self.motor5_state_changed)
        # 更新界面所展示的值
        self.update_hex_val()
        # 获取静态表.bin文件和静态表长度
        self.totalStatic_pushButton.clicked.connect(self.get_static_length)
        # 获取总动作表.bin文件以及长度
        self.totalAction_pushButton.clicked.connect(self.get_total_action)
        # 获取总动态表的.bin文件以及长度
        self.totalDynamic_pushButton.clicked.connect(self.get_total_dynamic)
        # 获取总监控表的.bin文件以及长度
        self.totalMonitoring_pushButton.clicked.connect(self.get_total_monitoring)
        # 获取总表的长度和十六进制值
        self.total_pushButton.clicked.connect(self.get_total_Length)
        # 生成表头
        self.tableHead_pushButton.clicked.connect(self.generate_table_head_bin)
        # 生成总表
        self.totalTable_pushButton.clicked.connect(self.generate_total_table_bin)
        # 生成最后的表头+3总表
        self.head_total_pushButton.clicked.connect(self.generate_finally_total_table_bin)

    def update_hex_val(self):
        """
        将十六进制值在界面上更新
        :return:
        """
        # 电机选择
        self.motor_hex_str = self.motor_selection_hex[2:] + self.motor_selection_hex[0:2]
        self.motorHex_lineEdit.setText(self.motor_hex_str)

    def motor1_state_changed(self, state):
        if state == 2:
            self.motor1_val = "11"
        else:
            self.motor1_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor2_state_changed(self, state):
        if state == 2:
            self.motor2_val = "11"
        else:
            self.motor2_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor3_state_changed(self, state):
        if state == 2:
            self.motor3_val = "11"
        else:
            self.motor3_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor4_state_changed(self, state):
        if state == 2:
            self.motor4_val = "11"
        else:
            self.motor4_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def motor5_state_changed(self, state):
        if state == 2:
            self.motor5_val = "11"
        else:
            self.motor5_val = "00"
        # 获取配置参数的16进制编码
        self.motor_selection_hex = self.get_motor_selection_hex()
        # 更新界面所展示的值
        self.update_hex_val()

    def get_motor_selection_hex(self):
        """
        返回电机配置值对应的十六进制
        :return:
        """
        val = self.motor5_val + self.motor4_val + self.motor3_val + self.motor2_val + self.motor1_val
        binary_str = "1100" + val + "00"
        # 提取前8个字符和后8个字符
        part1 = binary_str[:8]
        part2 = binary_str[8:]
        # 转换为十六进制，并确保每个部分是两个字符
        hex1 = format(int(part1, 2), '02X')
        hex2 = format(int(part2, 2), '02X')
        return hex1 + hex2

    def get_static_length(self):
        """
        读取文件夹下的以 ST 开头且文件名包含 '静态表' 的 .bin 文件，并计算字节数和内容
        获取静态表字节数和内容
        :return：
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        file_path = filedialog.askopenfilename(
            title="选择 .bin 文件",
            filetypes=[("二进制文件", "*.bin"), ("所有文件", "*.*")]
        )

        if not file_path:
            print("未选择任何文件")
            return
        # 筛选符合条件的文件
        if os.path.basename(file_path).startswith('ST') and '静态表' in os.path.basename(file_path):
            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_length = len(file_content)
                file_length_str = str(file_length)  # 将文件字节数转换为字符串
                file_content_hex = file_content.hex().upper()  # 转换为十六进制字符串

                print(f"文件: {os.path.basename(file_path)}")
                print(f"静态表字节数: {file_length}")
                # print(f"内容字符串: {file_content_hex}")
        else:
            print("未找到符合条件的 .bin 文件")
        self.static_length = file_length
        self.static_content_hex = file_content_hex
        # 更新 GUI 元素
        self.staticTable_lineEdit.setText(file_length_str)
        self.static_val_hex = self.calculate_hex_string(0)
        self.lineEdit_7.setText(self.static_val_hex)

    def calculate_hex_string(self, length):
        """
        计算静态表、总动作表、总动态表、总监控表的十六进制值
        :param length:
        :return:
        """
        # 基础值
        base_value = 2181038080
        # 计算总和
        total_value = base_value + length
        # 转换为十六进制（8位，不足位数前补0）
        hex_value = format(total_value, '08X')
        # 提取部分
        part1 = hex_value[6:8]  # 第 7 和第 8 位
        part2 = hex_value[4:6]  # 第 5 和第 6 位
        part3 = hex_value[2:4]  # 第 3 和第 4 位
        part4 = hex_value[0:2]  # 第 1 和第 2 位
        # 拼接结果
        result = (part1 + part2 + part3 + part4) * 3  # 重复三次
        return result

    def total_length_format_hex(self, total_length):
        """
        计算总表的十六进制值
        :param total_length:
        :return:
        """
        # 转换为十六进制，确保长度为 8 位，不足的前面补零
        hex_value = format(total_length, '08X')
        # 提取各部分
        part1 = hex_value[6:8]  # 第 7 和第 8 位
        part2 = hex_value[4:6]  # 第 5 和第 6 位
        part3 = hex_value[2:4]  # 第 3 和第 4 位
        part4 = hex_value[0:2]  # 第 1 和第 2 位
        # 拼接结果
        result = (part1 + part2 + part3 + part4) * 3  # 重复三次
        return result

    def get_total_action(self):
        """
        读取文件夹下所有以 AT 开头且包含四位十六进制数的 .bin 文件，拼接其内容为十六进制字符串，并计算总字节数
        :return:
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        folder_path = filedialog.askdirectory(
            title="选择 .bin 文件"
        )

        if not folder_path:
            print("未选择任何文件夹")
            return

        total_hex_content = ''
        total_length = 0

        # 正则表达式匹配以四位十六进制数
        pattern = re.compile(r'AT.*?([0-9A-Fa-f]{4}).*?\.bin$')

        # 遍历文件夹中的文件
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith('.bin') and pattern.match(filename):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'rb') as file:
                        file_content = file.read()
                        file_content_hex = file_content.hex().upper()  # 转换为十六进制字符串
                        total_hex_content += file_content_hex
                        total_length += len(file_content)
        # 动作表长度
        total_length_str = str(total_length)  # 将文件字节数转换为字符串
        self.action_length = total_length
        # 动作表内容
        self.action_content_hex = total_hex_content
        # 更新 GUI 元素
        self.actionTable_lineEdit.setText(total_length_str)
        self.action_val_hex = self.calculate_hex_string(self.static_length)
        self.lineEdit_8.setText(self.action_val_hex)
        print(f"动作表总字节数: {total_length}")
        # print(f"拼接后的十六进制字符串: {total_hex_content}")

        # ------------生成总的动作表.bin文件------------
        if len(self.action_content_hex) == 0:
            return
        # 文件夹不存在则创建
        base_path = os.path.abspath('./total_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成总动作表的.bin文件
        output_file_path = base_path + os.path.sep + '总动作表' + '.bin'
        # 将十六进制字符串转换为字节对象
        hex_bytes = bytes.fromhex(self.action_content_hex)
        # 将字节写入二进制文件
        with open(output_file_path, 'wb') as binary_file:
            binary_file.write(hex_bytes)


    def get_total_dynamic(self):
        """
        读取文件夹下所有以 DT 开头且包含四位数的 .bin 文件，拼接其内容为十六进制字符串，并计算总字节数
        :return:
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        folder_path = filedialog.askdirectory(
            title="选择 .bin 文件"
        )

        if not folder_path:
            print("未选择任何文件夹")
            return

        total_hex_content = ''
        total_length = 0

        # 正则表达式匹配以四位数字
        pattern = re.compile(r'DT.*?(\d{4}).*?\.bin$')

        # 遍历文件夹中的文件
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith('.bin') and pattern.match(filename):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'rb') as file:
                        file_content = file.read()
                        file_content_hex = file_content.hex().upper()  # 转换为十六进制字符串
                        total_hex_content += file_content_hex
                        total_length += len(file_content)
        # 动态表长度
        total_length_str = str(total_length)  # 将文件字节数转换为字符串
        self.dynamic_length = total_length
        # 动作表内容
        self.dynamic_content_hex = total_hex_content
        # 更新 GUI 元素
        self.dynamicTable_lineEdit.setText(total_length_str)
        self.dynamic_val_hex = self.calculate_hex_string(self.static_length + self.action_length)
        self.lineEdit_9.setText(self.dynamic_val_hex)
        print(f"动态表总字节数: {total_length}")

        # ------------生成总的动态表.bin文件------------
        if len(self.dynamic_content_hex) == 0:
            return
        # 文件夹不存在则创建
        base_path = os.path.abspath('./total_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成总动态表的.bin文件
        output_file_path = base_path + os.path.sep + '总动态表' + '.bin'
        # 将十六进制字符串转换为字节对象
        hex_bytes = bytes.fromhex(self.dynamic_content_hex)
        # 将字节写入二进制文件
        with open(output_file_path, 'wb') as binary_file:
            binary_file.write(hex_bytes)

    def get_total_monitoring(self):
        """
        读取文件夹下的以 zt 开头的 .bin 文件，并计算字节数和内容
        :return:
        """
        # 打开文件夹选择对话框
        Tk().withdraw()  # 隐藏主窗口
        file_path = filedialog.askopenfilename(
            title="选择 .bin 文件",
            filetypes=[("二进制文件", "*.bin"), ("所有文件", "*.*")]
        )

        if not file_path:
            print("未选择任何文件")
            return
        # 获取文件名
        filename = os.path.basename(file_path)
        # 筛选符合条件的文件
        if filename.startswith('zt') and filename.endswith('.bin'):
            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_length = len(file_content)
                file_length_str = str(file_length)  # 将文件字节数转换为字符串
                file_content_hex = file_content.hex().upper()  # 转换为十六进制字符串

                print(f"文件: {os.path.basename(file_path)}")
                print(f"字节数: {file_length}")
                # print(f"监控表内容: {file_content_hex}")
        else:
            print("未找到符合条件的 .bin 文件")
        self.monitoring_length = file_length
        self.monitoring_content_hex = file_content_hex
        # 更新 GUI 元素
        self.monitoringTable_lineEdit.setText(file_length_str)
        self.monitoring_val_hex = self.calculate_hex_string(self.static_length+self.action_length+self.dynamic_length)
        self.lineEdit_10.setText(self.monitoring_val_hex)

    def get_total_Length(self):
        """
        得到总表长度以及十六进制参数值
        :return:
        """
        self.total_table_length = self.static_length + self.action_length + self.dynamic_length + self.monitoring_length
        total_table_length_str = str(self.total_table_length)
        self.totalTable_lineEdit.setText(total_table_length_str)
        self.total_table_length_val_hex = self.total_length_format_hex(self.total_table_length)
        self.lineEdit_11.setText(self.total_table_length_val_hex)

    def generate_table_head_bin(self):
        """
        生成表头.bin文件
        :return:
        """
        self.table_head_hex = (self.total_table_config + self.motor_hex_str + self.static_val_hex + self.action_val_hex +
                               self.dynamic_val_hex + self.monitoring_val_hex + self.total_table_length_val_hex)
        # print(f"表头: {self.table_head_hex}")
        # 将生成的表头写入文件
        if len(self.table_head_hex) == 8:
            QMessageBox.information(None, "Success", "没有表头需要生成，请先获取其他表数据！")
            return
        # 文件夹不存在则创建
        base_path = os.path.abspath('./total_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成静态表的.bin文件
        output_file_path = base_path + os.path.sep + '表头' + '.bin'
        hex_string_to_binary_file(self.table_head_hex, output_file_path)
        print(f"表头生成成功！\n文件所在目录：{base_path}")
        QMessageBox.information(None, "Success", f"表头生成成功！\n文件所在目录：{base_path}")

    def generate_total_table_bin(self):
        """
        生成总表.bin文件
        :return:
        """
        # 总表 = 静态表 + 总动作表 + 总动态表 + 总监控表
        self.total_table_hex = self.static_content_hex + self.action_content_hex + self.dynamic_content_hex + self.monitoring_content_hex
        # 将生成的总表写入文件
        if len(self.total_table_hex) == 0:
            QMessageBox.information(None, "Success", "没有总表需要生成！")
            return
        # 文件夹不存在则创建
        base_path = os.path.abspath('./total_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成总表的.bin文件
        output_file_path = base_path + os.path.sep + '总表' + '.bin'
        hex_string_to_binary_file(self.total_table_hex, output_file_path)
        print(f"总表生成成功！\n文件所在目录：{base_path}")
        QMessageBox.information(None, "Success", f"总表生成成功！\n文件所在目录：{base_path}")

    def generate_finally_total_table_bin(self):
        """
        生成最终需要的总表 + 3总表.bin文件
        :return:
        """
        self.table_head_hex = (self.total_table_config + self.motor_hex_str + self.static_val_hex + self.action_val_hex +
                    self.dynamic_val_hex + self.monitoring_val_hex + self.total_table_length_val_hex)
        self.total_table_hex = self.static_content_hex + self.action_content_hex + self.dynamic_content_hex + self.monitoring_content_hex
        # 最终总表 = 表头 + 总表*3
        self.finally_total_table_hex = self.table_head_hex + self.total_table_hex*3
        if len(self.total_table_hex) == 0:
            QMessageBox.information(None, "Success", "没有总表+3总表需要生成！")
            return
        # 将生成的表头+3总表写入文件
        # 文件夹不存在则创建
        base_path = os.path.abspath('./total_bin')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        # 生成总表的.bin文件
        output_file_path = base_path + os.path.sep + '表头+3总表' + '.bin'
        hex_string_to_binary_file(self.finally_total_table_hex, output_file_path)
        print(f"总表+3总表生成成功！\n文件所在目录：{base_path}")
        QMessageBox.information(None, "Success", f"总表+3总表生成成功！\n文件所在目录：{base_path}")
        # 关闭窗口
        self.close()



