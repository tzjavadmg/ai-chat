from contextlib import contextmanager
from mysql.connector import pooling

# 创建一个连接池实例
dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "ai_chat",
}

_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)


@contextmanager
def open_cursor():
    connection = _pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()
        connection.commit()
        connection.close()

# class PooledConnection:
#     def __init__(self):
#         self.pool = _pool

#     def __enter__(self):
#         self.conn = self.pool.get_connection()
#         return self.conn

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.close()
