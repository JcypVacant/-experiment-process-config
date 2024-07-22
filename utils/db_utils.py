import sqlite3 as sqlite

def create_connection():
    """ 创建数据库连接 """
    conn = sqlite.connect('experimental-flow.db')
    return conn

def create_table(conn):
    """ 创建表 dynamic_num """
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dynamic_num (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dynamic_id INTEGER
    )
    ''')

    """ 创建表 experiment_flow """
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

def insert_experiment_flow(conn, start_time, action_id, action_time):
    """ 插入 experiment_flow 记录 """
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

if __name__ == '__main__':
    # 创建数据库连接
    conn = create_connection()
    # 关闭连接
    conn.close()
