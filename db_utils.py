import os
import pandas as pd

def format_start_time(start_time):
    """ 将 start_time 转换为十六进制并反转 """
    hex_start_time = format(start_time, '08X')
    reversed_hex_start_time = ''.join([hex_start_time[i:i+2] for i in range(0, len(hex_start_time), 2)][::-1])
    return reversed_hex_start_time

def format_action_id(action_id):
    """ 将 action_id 字符串反转 """
    reversed_hex_action_id = ''.join([action_id[i:i + 2] for i in range(0, len(action_id), 2)][::-1])
    return reversed_hex_action_id

def format_action_time(action_time):
    """ 将 action_time 转换为十六进制并格式化 """
    hex_action_time = format(action_time, '04X')
    return hex_action_time

def process_dynamic_info_records(records):
    """ 处理 process_dynamic_info_records 记录 """
    processed_records = []
    for record in records:
        start_time, action_id, action_time = record
        formatted_start_time = format_start_time(start_time)
        formatted_action_id = format_action_id(action_id)
        formatted_action_time = format_action_time(action_time)
        processed_records.append((formatted_start_time, formatted_action_id, formatted_action_time))
    return processed_records

def format_four_digits(dynamic_id):
    """ 将 dynamic_id 格式化为四位数字 """
    return f"{dynamic_id:04d}"
def format_dynamic_id(dynamic_id):
    """ 将 dynamic_id 字符串反转 """
    reversed_hex_dynamic_id = ''.join([dynamic_id[i:i + 2] for i in range(0, len(dynamic_id), 2)][::-1])
    return reversed_hex_dynamic_id

def format_max_action(max_action_num):
    """ 将 max_action_num 转换为十六进制并反转 """
    hex_max_action_num = format(max_action_num, '012X')
    reversed_hex_max_action_num = ''.join([hex_max_action_num[i:i+2] for i in range(0, len(hex_max_action_num), 2)][::-1])
    return reversed_hex_max_action_num

def save_to_excel(data, filename):
    """ 保存记录到 Excel 文件 """
    # 创建 DataFrame
    df = pd.DataFrame(data)
    # 文件夹不存在则创建
    base_path = os.path.abspath('./dynamic_bin')
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    output_file_path = base_path + os.path.sep + filename
    df.to_excel(output_file_path, index=False,  header=False)
    print(f"Excel文件所在目录：{output_file_path}")



