# def calculate_hex_string(d4):
#     # 基础值
#     base_value = 2181038080
#
#     # 计算总和
#     total_value = base_value + d4
#
#     # 转换为十六进制（8位，不足位数前补0）
#     hex_value = format(total_value, '08X')
#
#     # 提取部分
#     part1 = hex_value[6:8]  # 第 7 和第 8 位
#     part2 = hex_value[4:6]  # 第 5 和第 6 位
#     part3 = hex_value[2:4]  # 第 3 和第 4 位
#     part4 = hex_value[0:2]  # 第 1 和第 2 位
#
#     # 拼接结果
#     result = (part1 + part2 + part3 + part4) * 3  # 重复三次
#     return result
#
#
# # 示例值
# d4 = 5676 + 30426 + 103200
#
# # 计算结果
# result = calculate_hex_string(d4)
# print(result)
# def format_hex_string(d8):
#     # 转换为十六进制，确保长度为 8 位，不足的前面补零
#     hex_value = format(d8, '08X')
#
#     # 提取各部分
#     part1 = hex_value[6:8]  # 第 7 和第 8 位
#     part2 = hex_value[4:6]  # 第 5 和第 6 位
#     part3 = hex_value[2:4]  # 第 3 和第 4 位
#     part4 = hex_value[0:2]  # 第 1 和第 2 位
#
#     # 拼接结果
#     result = (part1 + part2 + part3 + part4) * 3  # 重复三次
#     return result
#
#
# # 示例值
# d8 = 140182  # 替换为实际的 D8 值
#
# # 计算结果
# result = format_hex_string(d8)
# print(result)
import sqlite3

# 连接到数据库
conn = sqlite3.connect('experimental-flow.db')
cursor = conn.cursor()

# 列出所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# 关闭连接
conn.close()
