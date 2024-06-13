import sqlite3
from models.crud_operations import CRUDOperations
from services.book_service import BookService
from models.book import Book
def main():
    # db = sqlite3.connect('database.db')
    # crud = CRUDOperations(db)
    # book_service = BookService(db)

    while True:
        print("1. Create Author")
        print("2. Delete Author")
        print("3. Create Book")
        print("4. Delete Book")
        print("5. Create Genre")
        print("6. Delete Genre")
        print("7. Display Books with Authors and Genres")
        print("8. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError as e:
            print(f"Invalid input. Please enter a number between 1 and 8. Error: {e}")
            continue

        if choice == 1:
            name = input("Enter author name: ")
            email = input("Enter author email: ")
            CRUDOperations.create_author(name, email)
    
        elif choice == 2:
            try:
                author_id = int(input("Enter author ID: "))
                CRUDOperations.delete_author(author_id)
            except ValueError as e:
                print(f"Invalid input. Author ID should be a number. Error: {e}")
    
        elif choice == 3:
            CRUDOperations.create_book_with_input()
    
        elif choice == 4:
            try:
                book_id = int(input("Enter book ID: "))
                CRUDOperations.delete_book(book_id)
            except ValueError as e:
                print(f"Invalid input. Book ID should be a number. Error: {e}")
    
        elif choice == 5:
            genre_name = input("Enter genre name: ")
            CRUDOperations.create_genre(genre_name)
    
        elif choice == 6:
            try:
                genre_id = int(input("Enter genre ID: "))
                CRUDOperations.delete_genre(genre_id)
            except ValueError as e:
                print(f"Invalid input. Genre ID should be a number. Error: {e}")
    
        elif choice == 7:
            Book.get_all_with_authors()

        elif choice == 8:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    
    # db.close()

if __name__ == "__main__":
    print("Debug: Starting main function")
    main()
    print("Debug: Exiting main function")
