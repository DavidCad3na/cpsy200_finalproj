class CategoryList:
    def __init__(self, categories):
        self.categories = categories

    def view_category(self, category_id):
        return self.categories.get(category_id, None)

    def add_category(self, category_id, category_name):
        self.categories[category_id] = category_name

    def remove_category(self, category_id):
        if category_id in self.categories:
            del self.categories[category_id]
        