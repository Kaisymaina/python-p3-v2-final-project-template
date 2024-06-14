from orm.orm import ORM

class Book:
    orm = ORM('library.db')

    @classmethod
    def create(cls, title, description, author_id, genre_id):
        try:
            cls.orm.execute('INSERT INTO books (title, description, author_id, genre_id) VALUES (?, ?, ?, ?)', 
                            (title, description, author_id, genre_id))
            print("Book created successfully.")
        except Exception as e:
            print(f"Error creating book: {e}")

    @classmethod
    def get_all(cls):
        try:
            books = cls.orm.fetchall(
                'SELECT books.id, books.title, books.description, authors.name, genres.name '
                'FROM books '
                'JOIN authors ON books.author_id = authors.id '
                'JOIN genres ON books.genre_id = genres.id'
            )
            return books
        except Exception as e:
            print(f"Error fetching books: {e}")
            return []

    @classmethod
    def delete(cls, book_id):
        try:
            cls.orm.execute('DELETE FROM books WHERE id = ?', (book_id,))
            print("Book deleted successfully.")
        except Exception as e:
            print(f"Error deleting book: {e}")
