# models/crud_operations.py

import sqlite3

class CRUDOperations:
    # def __init__(self, db):
    #     self.db = db
    #     self.create_tables()

    def create_tables(self):
        try:
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS author (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author_name TEXT,
                    email TEXT
                )
            """)
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS book (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    author_id INTEGER,
                    genre_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES author (author_id) ON DELETE CASCADE,
                    FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE CASCADE
                )
            """)
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS genre (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_name TEXT
                )
            """)
            self.db.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating tables: {e}")

    def create_author(self, name, email):
        try:
            cursor = self.db.execute("INSERT INTO author (author_name, email) VALUES (?,?)", (name, email))
            self.db.commit()
            if cursor.lastrowid:
                print(f"Author created successfully with ID {cursor.lastrowid}!")
            else:
                print("Failed to create author.")
        except sqlite3.Error as e:
            print(f"An error occurred while creating author: {e}")

    def delete_author(self, author_id):
        try:
            cursor = self.db.execute("SELECT * FROM book WHERE author_id=?", (author_id,))
            books = cursor.fetchall()
            if books:
                print("Cannot delete author. There are books associated with this author.")
            else:
                cursor = self.db.execute("DELETE FROM author WHERE author_id=?", (author_id,))
                self.db.commit()
                if cursor.rowcount:
                    print("Author deleted successfully!")
                else:
                    print("Failed to delete author or author not found.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting author: {e}")

    def create_book(self, title, description, author_id, genre_id):
        try:
            cursor = self.db.execute("INSERT INTO book (title, description, author_id, genre_id) VALUES (?,?,?,?)", (title, description, author_id, genre_id))
            self.db.commit()
            if cursor.lastrowid:
                print(f"Book created successfully with ID {cursor.lastrowid}!")
            else:
                print("Failed to create book.")
        except sqlite3.Error as e:
            print(f"An error occurred while creating book: {e}")

    def delete_book(self, book_id):
        try:
            cursor = self.db.execute("DELETE FROM book WHERE book_id=?", (book_id,))
            self.db.commit()
            if cursor.rowcount:
                print("Book deleted successfully!")
            else:
                print("Failed to delete book or book not found.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting book: {e}")

    def create_genre(self, genre_name):
        try:
            cursor = self.db.execute("INSERT INTO genre (genre_name) VALUES (?)", (genre_name,))
            self.db.commit()
            if cursor.lastrowid:
                print(f"Genre created successfully with ID {cursor.lastrowid}!")
            else:
                print("Failed to create genre.")
        except sqlite3.Error as e:
            print(f"An error occurred while creating genre: {e}")

    def delete_genre(self, genre_id):
        try:
            cursor = self.db.execute("SELECT * FROM book WHERE genre_id=?", (genre_id,))
            books = cursor.fetchall()
            if books:
                print("Cannot delete genre. There are books associated with this genre.")
            else:
                cursor = self.db.execute("DELETE FROM genre WHERE genre_id=?", (genre_id,))
                self.db.commit()
                if cursor.rowcount:
                    print("Genre deleted successfully!")
                else:
                    print("Failed to delete genre or genre not found.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting genre: {e}")

    def create_book_with_input(self):
        title = input("Enter book title: ")
        description = input("Enter book description: ")
        try:
            author_id = int(input("Enter author ID: "))
            genre_id = int(input("Enter genre ID: "))
            self.create_book(title, description, author_id, genre_id)
        except ValueError as e:
            print(f"Invalid input. Author ID and Genre ID should be numbers. Error: {e}")
