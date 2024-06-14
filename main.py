# main.py

import sqlite3
from models.book import Book
from models.author import Author
from models.genre import Genre
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_db():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            author_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        print("Database 'library.db' initialized successfully.")

def main_menu():
    clear_screen()
    print("Library Management CLI")
    print("===================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Add Author")
    print("5. View Authors")
    print("6. Delete Author")
    print("7. Add Genre")
    print("8. View Genres")
    print("9. Delete Genre")
    print("10. Exit")

    choice = input("Enter your choice: ")
    return choice

def add_book():
    title = input("Enter the book title: ")
    description = input("Enter the book description: ")
    author_id = input("Enter the author ID: ")
    genre_id = input("Enter the genre ID: ")
    try:
        Book.create(title, description, int(author_id), int(genre_id))
        print("Book added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

def view_books():
    try:
        books = Book.get_all()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Description: {book[2]}, Author ID: {book[3]}, Genre ID: {book[4]}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error fetching books: {e}")

def delete_book():
    book_id = input("Enter the book ID to delete: ")
    try:
        Book.delete(int(book_id))
        print("Book deleted successfully.")
    except Exception as e:
        print(f"Error deleting book: {e}")

def add_author():
    name = input("Enter the author name: ")
    try:
        Author.create(name)
        print("Author added successfully.")
    except Exception as e:
        print(f"Error adding author: {e}")

def view_authors():
    try:
        authors = Author.get_all()
        if authors:
            for author in authors:
                print(f"ID: {author[0]}, Name: {author[1]}")
        else:
            print("No authors found.")
    except Exception as e:
        print(f"Error fetching authors: {e}")

def delete_author():
    author_id = input("Enter the author ID to delete: ")
    try:
        Author.delete(int(author_id))
        print("Author deleted successfully.")
    except Exception as e:
        print(f"Error deleting author: {e}")

def add_genre():
    name = input("Enter the genre name: ")
    try:
        Genre.create(name)
        print("Genre added successfully.")
    except Exception as e:
        print(f"Error adding genre: {e}")

def view_genres():
    try:
        genres = Genre.get_all()
        if genres:
            for genre in genres:
                print(f"ID: {genre[0]}, Name: {genre[1]}")
        else:
            print("No genres found.")
    except Exception as e:
        print(f"Error fetching genres: {e}")

def delete_genre():
    genre_id = input("Enter the genre ID to delete: ")
    try:
        Genre.delete(int(genre_id))
        print("Genre deleted successfully.")
    except Exception as e:
        print(f"Error deleting genre: {e}")

def main():
    initialize_db()  # Initialize or update database schema

    while True:
        choice = main_menu()
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            add_author()
        elif choice == '5':
            view_authors()
        elif choice == '6':
            delete_author()
        elif choice == '7':
            add_genre()
        elif choice == '8':
            view_genres()
        elif choice == '9':
            delete_genre()
        elif choice == '10':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press Enter to continue...")

if __name__ == '__main__':
    main()
