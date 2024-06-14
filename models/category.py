from orm.orm import ORM

class Category:
    orm = ORM('library.db')

    @classmethod
    def create(cls, name):
        try:
            cls.orm.execute('INSERT INTO categories (name) VALUES (?)', (name,))
            print("Category created successfully.")
        except Exception as e:
            print(f"Error creating category: {e}")

    @classmethod
    def get_all(cls):
        try:
            categories = cls.orm.fetchall('SELECT * FROM categories')
            return categories
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return []

    @classmethod
    def delete(cls, category_id):
        try:
            cls.orm.execute('DELETE FROM categories WHERE id = ?', (category_id,))
            print("Category deleted successfully.")
        except Exception as e:
            print(f"Error deleting category: {e}")
