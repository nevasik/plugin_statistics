import psycopg2
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(**DATABASE_CONFIG)

    def execute_query(self, query, params=()):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result

    def close(self):
        self.connection.close()
