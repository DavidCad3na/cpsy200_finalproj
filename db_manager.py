import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="sql5.freesqldatabase.com",
            user="sql5773273",
            password="7c98kZDGKx",
            database="sql5773273",
            port=3306
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values or ())
        self.connection.commit()

    def fetch_query(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
