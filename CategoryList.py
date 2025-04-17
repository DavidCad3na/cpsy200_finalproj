# Connor Yasinski

class CategoryList:
    def __init__(self, db):
        self.db = db

    def viewCategory(self):
        query = "SELECT categoryId, category_name FROM categories"
        categories = self.db.fetch_query(query)
        if not categories:
            print("No categories found.")
        else:
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}")

    def addCategory(self, category_id, category_name):
        query = "INSERT INTO categories (categoryId, category_name) VALUES (%s, %s)"
        self.db.execute_query(query, (category_id, category_name))
        print(f"Category '{category_name}' with ID {category_id} added successfully.")

    def removeCategory(self, category_id):
        query = "DELETE FROM categories WHERE categoryId = %s"
        self.db.execute_query(query, (category_id,))
        print(f"Category with ID {category_id} removed successfully.")
