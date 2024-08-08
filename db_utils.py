import os
import sqlite3 as sqlite
import pandas as pd
import numpy

def create_connection():
    """ 创建数据库连接 """
    conn = sqlite.connect('experimental-flow.db')
    return conn

def create_table(conn):
    """ 创建表 dynamic_num 和 experiment_flow """
    cursor = conn.cursor()

    # 创建表 dynamic_num
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dynamic_num (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dynamic_id INTEGER
    )
    ''')

    # 创建表 experiment_flow
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS experiment_flow (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time INTEGER,
            action_id TEXT,
            action_time INTEGER
        )
        ''')
    conn.commit()

def insert_dynamic_num(conn, dynamic_id):
    """ 插入 dynamic_num 记录 """
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dynamic_num (dynamic_id) VALUES (?)', (dynamic_id,))
    conn.commit()

def fetch_dynamic_num_by_id(conn):
    """查询id等于1的dynamic_id记录"""
    cursor = conn.cursor()
    id = 1
    cursor.execute('SELECT * FROM dynamic_num WHERE id = ?', (id,))
    return cursor.fetchone()
def update_dynamic_id_by_id(conn):
    """ 更新 id 等于给定值的 dynamic_id 加1 """
    cursor = conn.cursor()
    id = 1
    cursor.execute('UPDATE dynamic_num SET dynamic_id = dynamic_id + 1 WHERE id = ?', (id,))
    conn.commit()

def insert_experiment_flow(conn, start_time, action_id, action_time):
    """ 插入 experiment_flow 记录 """
    action_id = action_id.upper()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO experiment_flow (start_time, action_id, action_time) VALUES (?, ?, ?)',
                   (start_time, action_id, action_time))
    conn.commit()

    # 检查是否需要插入额外的记录
    if action_time == 65535:
        # 查询已插入的记录数
        cursor.execute('SELECT COUNT(*) FROM experiment_flow')
        count = cursor.fetchone()[0]

        # 计算需要插入的额外记录数
        if count < 128:
            records_to_insert = 128 - count
            for _ in range(records_to_insert):
                cursor.execute('INSERT INTO experiment_flow (start_time, action_id, action_time) VALUES (?, ?, ?)',
                               (4294967295, 'FFFF', 65535))
            conn.commit()

def fetch_all_dynamic_num(conn):
    """ 查询所有 dynamic_num 记录 """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dynamic_num')
    return cursor.fetchall()

def fetch_all_experiment_flow(conn):
    """ 查询所有 experiment_flow 记录 """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM experiment_flow')
    return cursor.fetchall()

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

def process_experiment_flow_records(records):
    """ 处理 experiment_flow 记录 """
    processed_records = []
    for record in records:
        record_id, start_time, action_id, action_time = record
        formatted_start_time = format_start_time(start_time)
        formatted_action_id = format_action_id(action_id)
        formatted_action_time = format_action_time(action_time)
        processed_records.append((record_id, formatted_start_time, formatted_action_id, formatted_action_time))
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

def delete_all_experiment_flow_data(conn):
    """ 删除 experiment_flow 表中的所有数据 """
    cursor = conn.cursor()
    cursor.execute('DELETE FROM experiment_flow')
    conn.commit()

def drop_experiment_flow_table(conn):
    """ 删除 experiment_flow 表 """
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS experiment_flow')
    conn.commit()


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
    print(f"数据已保存到 {output_file_path}")

# def read_bin_files_to_string():
#     """读取文件夹中的 .bin 文件并将其内容转换为字符串"""
#     # 打开文件夹选择对话框
#     Tk().withdraw()  # 隐藏主窗口
#     folder_selected = filedialog.askdirectory()
#
#     if not folder_selected:
#         print("未选择文件夹。")
#         return
#
#     bin_files = [f for f in os.listdir(folder_selected) if f.endswith('.bin')]
#     if not bin_files:
#         print("文件夹中没有 .bin 文件。")
#         return
#
#     bin_contents = {}
#
#     for bin_file in bin_files:
#         file_path = os.path.join(folder_selected, bin_file)
#         with open(file_path, 'rb') as file:
#             binary_data = file.read()
#             hex_string = binary_data.hex().upper()  # 将二进制数据转换为十六进制字符串
#             bin_contents[bin_file] = hex_string
#
#     return bin_contents
    # 创建数据库连接
    conn = create_connection()
    create_table(conn)
    # 示例调用
    # bin_files_contents = read_bin_files_to_string()
    #
    # # 打印结果
    # if bin_files_contents:
    #     for file_name, content in bin_files_contents.items():
    #         print(f"File: {file_name}, Content: {content}")
    #insert_experiment_flow(conn, 20, '6021', 0)
    #insert_experiment_flow(conn, 490800, 'd000', 65535)  # 示例插入

    # 查询并处理所有记录
    # experiment_flow_records = fetch_all_experiment_flow(conn)
    # processed_records = process_experiment_flow_records(experiment_flow_records)
    #
    # dynamic_id = 90
    #
    # MAX_ACTION_NUM = 128
    # excel_records = []
    # excel_records.append((dynamic_id, MAX_ACTION_NUM, ' '))
    # for record in experiment_flow_records:
    #     record_id, start_time, action_id, action_time = record
    #     excel_records.append((start_time, action_id, action_time))
    # print(excel_records)
    # # 格式化动态ID
    # val = format_four_digits(dynamic_id)
    # # 将 val 字符串反转
    # rel = format_action_id(val)
    # print(rel)
    # # 将最大动作数转换为十六进制并反转
    # max_action_hex = format_max_action(MAX_ACTION_NUM)
    # print(max_action_hex)
    # dynamic_hex_list = []
    # dynamic_hex_list.append(rel)
    # dynamic_hex_list.append(max_action_hex)
    # # 打印处理后的记录
    # print("Processed experiment_flow records:")
    # for record in processed_records:
    #     record_id, formatted_start_time, formatted_action_id, formatted_action_time = record
    #     dynamic_hex = formatted_start_time + formatted_action_id + formatted_action_time
    #     dynamic_hex_list.append(dynamic_hex)
    #     print(dynamic_hex)
    #
    # # 将所有十六进制字符串拼接成一个大的十六进制字符串
    # combined_hex_string = ''.join(dynamic_hex_list)
    # print(combined_hex_string)
    #
    # # 关闭连接
    # conn.close()
    # # 文件夹不存在则创建
    # base_path = os.path.abspath('./dynamic_bin')
    # if not os.path.exists(base_path):
    #     os.makedirs(base_path)
    #
    # output_file_path = base_path + os.path.sep + 'DT_' + val + '.bin'
    # hex_string_to_binary_file(combined_hex_string, output_file_path)
    # print(f"动态表生成成功！\n文件所在目录：{base_path}")
    # excel_filename = f'DT_{val}.xlsx'
    # save_to_excel(excel_records, excel_filename)
    # QMessageBox.information(None, "Success", f"动态表生成成功！\n文件所在目录：{base_path}")


