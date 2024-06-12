class Book:
    def __init__(self, book_id, title, author, genre, publication_date, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.price = price

    def __str__(self):
        return f"Book {self.title} by {self.author.name} (ID: {self.book_id})"

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author_id": self.author.author_id,
            "genre_id": self.genre.genre_id,
            "publication_date": self.publication_date,
            "price": self.price
        }