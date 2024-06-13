from tabulate import tabulate
from models.author import Author
from models.book import Book
from models.genre import Genre


Author.drop_table()
Author.create_table()
author1 = Author(None, 'J.K Rowling', 'rowlingsK@gmail.com')
author1.save()


Book.drop_table()
Book.create_table()
book1 = Book(None, 'Norwegian Wood', 'Melancholic tale of love and loss.', 5, 1)
book1.save()


Genre.drop_table()
Genre.create_table()
genre1 = Genre(None, 'Romance')
genre1.save()



books_with_authors = Book.get_all_with_authors()


table_data = []
for book in books_with_authors:
    table_data.append([
        book.id,
        book.title,
        book.description,
        book.genre_name,
        book.author_name,
        book.author_email
    ])

''
headers = ['ID', 'Title', 'Description', 'Genre Name', 'Author Name', 'Author Email']


print(tabulate(table_data, headers=headers, tablefmt='pretty')) 

