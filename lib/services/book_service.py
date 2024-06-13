

import sqlite3
from config.connection import CURSOR,CONN

class BookService:
    # def __init__(self, db):
    #     self.db = db
    @classmethod
    def get_books_with_author_genre(cls):
        try:
            cursor = CURSOR.execute("""
                SELECT books.book_id, books.book_title, books.book_description, author.author_name, genre.genre_name
                FROM books
                JOIN author ON books.author_id = author.author_id
                JOIN genre ON books.genre_id = genre.genre_id
            """)
            books = cursor.fetchall()
            for book in books:
                print(f"Book ID: {book[0]}, Title: {book[1]}, Description: {book[2]}, Author: {book[3]}, Genre: {book[4]}")
        except sqlite3.Error as e:
            print(f"An error occurred while fetching books: {e}")
