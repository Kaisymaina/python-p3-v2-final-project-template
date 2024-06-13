from config.connection import CONN, CURSOR


class Book:
    all = {}

    def __init__(self, book_id, book_title, book_description, author_id, genre_id):
        self.book_id = book_id
        self.book_title = book_title
        self.book_description = book_description
        self.author_id = author_id
        self.genre_id = genre_id

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS books"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_title TEXT,
            book_description TEXT,
            author_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(author_id),
            FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO books (
            book_title,
            book_description,
            author_id,
            genre_id
        ) VALUES (?,?,?,?)
        """
        CURSOR.execute(
            sql, (
                self.book_title,
                self.book_description,
                self.author_id,
                self.genre_id
            )
        )
        CONN.commit()
        self.book_id = CURSOR.lastrowid

    @classmethod
    def instance_from_db_with_authors(cls, row):
        book_id, book_title, book_description, genre_name, author_name, author_email = row
        book = cls.all.get(book_id)
        if book:
            book.book_id = book_id
            book.book_title = book_title
            book.book_description = book_description
            book.genre_name = genre_name
            book.author_name = author_name
            book.author_email = author_email
        else:
            book = cls(book_id, book_title, book_description, None, None)
            book.genre_name = genre_name
            book.author_name = author_name
            book.author_email = author_email
            cls.all[book_id] = book
        return book

    @classmethod
    def get_all_with_authors(cls):

        sql = """
        SELECT books.book_id, books.book_title, books.book_description, genre.genre_name, author.author_name, author.author_email
        FROM books
        JOIN author ON books.author_id = author.author_id
        JOIN genre ON books.genre_id = genre.genre_id
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        books_with_authors = []
        for row in rows:
            book = cls.instance_from_db_with_authors(row)
            books_with_authors.append(book)
        return books_with_authors




# Example usage
Book.drop_table()
Book.create_table()

book1 = Book(None, 'Norwegian Wood', 'Melancholic tale of love and loss.', 5, 1)
book1.save()

book2 = Book(None, 'Harry Potter', 'Young wizards adventures at magical school.', 1, 2)
book2.save()

book3 = Book(None, 'The Handmaids Tale', 'Dystopian future where women are subjugated.', 4, 3)
book3.save()

book4 = Book(None, 'IT', 'Terrifying shape-shifting clown haunts small town.', 3, 4)
book4.save()

book5 = Book(None, 'A Song of Ice and Fire', 'Epic fantasy of power, betrayal, and dragons.', 2, 5)
book5.save()

book6 = Book(None, 'Oryx and Crake','Dystopian tale of genetic engineering gone wrong.', 4, 3)
book6.save()

book7 = Book(None, 'Kafka on the Shore', 'Surreal exploration of identity and human connection.', 5, 6)
book7.save()

book8 = Book(None, 'The Shining', 'Family trapped in haunted hotels dark past.', 3, 4)
book8.save()

book9 = Book(None, 'Game of Thrones', 'Epic fantasy of power struggles and royal intrigue.', 2, 5)
book9.save()
