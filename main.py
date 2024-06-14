from models.book import Book
from models.author import Author
from models.category import Category
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Library Management CLI")
    print("===================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Add Author")
    print("6. View Authors")
    print("7. Update Author")
    print("8. Delete Author")
    print("9. Add Category")
    print("10. View Categories")
    print("11. Update Category")
    print("12. Delete Category")
    print("13. Exit")

    choice = input("Enter your choice: ")
    return choice

def add_book():
    title = input("Enter the book title: ")
    author_id = input("Enter the author ID: ")
    category_id = input("Enter the category ID: ")
    try:
        Book.create(title, int(author_id), int(category_id))
        print("Book added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

def view_books():
    try:
        books = Book.get_all()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category ID: {book[3]}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error fetching books: {e}")

def update_book():
    book_id = input("Enter the book ID to update: ")
    title = input("Enter the new title: ")
    author_id = input("Enter the new author ID: ")
    category_id = input("Enter the new category ID: ")
    try:
        Book.update(int(book_id), title, int(author_id), int(category_id))
        print("Book updated successfully.")
    except Exception as e:
        print(f"Error updating book: {e}")

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

def update_author():
    author_id = input("Enter the author ID to update: ")
    name = input("Enter the new name: ")
    try:
        Author.update(int(author_id), name)
        print("Author updated successfully.")
    except Exception as e:
        print(f"Error updating author: {e}")

def delete_author():
    author_id = input("Enter the author ID to delete: ")
    try:
        Author.delete(int(author_id))
        print("Author deleted successfully.")
    except Exception as e:
        print(f"Error deleting author: {e}")

def add_category():
    name = input("Enter the category name: ")
    try:
        Category.create(name)
        print("Category added successfully.")
    except Exception as e:
        print(f"Error adding category: {e}")

def view_categories():
    try:
        categories = Category.get_all()
        if categories:
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}")
        else:
            print("No categories found.")
    except Exception as e:
        print(f"Error fetching categories: {e}")

def update_category():
    category_id = input("Enter the category ID to update: ")
    name = input("Enter the new name: ")
    try:
        Category.update(int(category_id), name)
        print("Category updated successfully.")
    except Exception as e:
        print(f"Error updating category: {e}")

def delete_category():
    category_id = input("Enter the category ID to delete: ")
    try:
        Category.delete(int(category_id))
        print("Category deleted successfully.")
    except Exception as e:
        print(f"Error deleting category: {e}")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            add_author()
        elif choice == '6':
            view_authors()
        elif choice == '7':
            update_author()
        elif choice == '8':
            delete_author()
        elif choice == '9':
            add_category()
        elif choice == '10':
            view_categories()
        elif choice == '11':
            update_category()
        elif choice == '12':
            delete_category()
        elif choice == '13':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press Enter to continue...")

if __name__ == '__main__':
    main()
