from orm.orm import ORM

class Book:
    orm = ORM('library.db')

    @classmethod
    def create(cls, title, author_id, category_id):
        try:
            cls.orm.execute('INSERT INTO books (title, author_id, category_id) VALUES (?, ?, ?)', (title, author_id, category_id))
            print("Book created successfully.")
        except Exception as e:
            print(f"Error creating book: {e}")

    @classmethod
    def get_all(cls):
        try:
            books = cls.orm.fetchall(
                'SELECT books.id, books.title, authors.name, books.category_id '
                'FROM books '
                'JOIN authors ON books.author_id = authors.id'
            )
            return books
        except Exception as e:
            print(f"Error fetching books: {e}")
            return []

    @classmethod
    def update(cls, book_id, title, author_id, category_id):
        try:
            cls.orm.execute('UPDATE books SET title = ?, author_id = ?, category_id = ? WHERE id = ?', 
                            (title, author_id, category_id, book_id))
            print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")

    @classmethod
    def delete(cls, book_id):
        try:
            cls.orm.execute('DELETE FROM books WHERE id = ?', (book_id,))
            print("Book deleted successfully.")
        except Exception as e:
            print(f"Error deleting book: {e}")
