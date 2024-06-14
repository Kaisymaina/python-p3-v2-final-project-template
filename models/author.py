from orm.orm import ORM

class Author:
    orm = ORM('library.db')

    @classmethod
    def create(cls, name):
        try:
            cls.orm.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            print("Author created successfully.")
        except Exception as e:
            print(f"Error creating author: {e}")

    @classmethod
    def get_all(cls):
        try:
            authors = cls.orm.fetchall('SELECT * FROM authors')
            return authors
        except Exception as e:
            print(f"Error fetching authors: {e}")
            return []

    @classmethod
    def delete(cls, author_id):
        try:
            cls.orm.execute('DELETE FROM authors WHERE id = ?', (author_id,))
            print("Author deleted successfully.")
        except Exception as e:
            print(f"Error deleting author: {e}")
