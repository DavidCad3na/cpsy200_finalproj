# Connor Yasinski

class CategoryList:
    def __init__(self, db):
        self.db = db

    def viewCategory(self, category_id):
        query = "SELECT * FROM categories WHERE id = %s"
        result = self.db.fetch_query(query, (category_id,))
        if result:
            return result[0]  # Return the first matching category
        else:
            print(f"No category found with ID {category_id}.")
            return None

    def addCategory(self, category_id, category_name):
        query = "INSERT INTO categories (id, name) VALUES (%s, %s)"
        self.db.execute_query(query, (category_id, category_name))
        print(f"Category '{category_name}' with ID {category_id} added successfully.")

    def removeCategory(self, category_id):
        query = "DELETE FROM categories WHERE id = %s"
        self.db.execute_query(query, (category_id,))
        print(f"Category with ID {category_id} removed successfully.")
