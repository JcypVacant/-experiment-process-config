import sqlite3

# def initialize_database():
#     conn = sqlite3.connect('experimental-flow.db')
#     cursor = conn.cursor()
#     # 创建表 dynamic_num
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS dynamic_num (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             dynamic_id INTEGER
#         )
#         ''')
#
#     # 创建表 experiment_flow
#     cursor.execute('''
#             CREATE TABLE IF NOT EXISTS experiment_flow (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 start_time INTEGER,
#                 action_id TEXT,
#                 action_time INTEGER
#             )
#             ''')
#     conn.commit()
#     conn.close()
# import os
# import sqlite3
# import sys
#
#
# def get_database_path():
#     # 获取当前运行脚本的路径
#     if getattr(sys, 'frozen', False):
#         # 运行在打包环境中
#         base_path = sys._MEIPASS
#     else:
#         # 开发环境
#         base_path = os.path.dirname(__file__)
#     return os.path.join(base_path, 'experimental-flow.db')
#
# def connect_to_database():
#     db_path = get_database_path()
#     return sqlite3.connect(db_path)

# if __name__ == "__main__":
#     initialize_database()
