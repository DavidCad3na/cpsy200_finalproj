# Connor Yasinski
import mysql.connector

class CategoryList:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def view_category(self, category_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM categories WHERE id = %s"
        cursor.execute(query, (category_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def add_category(self, category_id, category_name):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO categories (id, name) VALUES (%s, %s)"
        cursor.execute(query, (category_id, category_name))
        self.db_connection.commit()
        cursor.close()

    def remove_category(self, category_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM categories WHERE id = %s"
        cursor.execute(query, (category_id,))
        self.db_connection.commit()
        cursor.close()