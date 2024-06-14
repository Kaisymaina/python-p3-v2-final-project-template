import click
from models.book import Book
from models.author import Author
from models.genre import Category

@click.group()
def cli():
    """CLI for managing library."""
    pass

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
@click.argument('category_id', type=int)
def add_book(title, author_id, category_id):
    """Add a new book."""
    try:
        Book.create(title, author_id, category_id)
        click.echo(f'Book "{title}" added.')
    except Exception as e:
        click.echo(f'Error adding book: {e}')

@cli.command()
def view_books():
    """View all books."""
    try:
        books = Book.get_all()
        for book in books:
            click.echo(f'ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Category ID: {book[3]}')
    except Exception as e:
        click.echo(f'Error fetching books: {e}')

@cli.command()
@click.argument('book_id', type=int)
@click.argument('title')
@click.argument('author_id', type=int)
@click.argument('category_id', type=int)
def update_book(book_id, title, author_id, category_id):
    """Update an existing book."""
    try:
        Book.update(book_id, title, author_id, category_id)
        click.echo(f'Book ID {book_id} updated.')
    except Exception as e:
        click.echo(f'Error updating book: {e}')

@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    """Delete a book."""
    try:
        Book.delete(book_id)
        click.echo(f'Book ID {book_id} deleted.')
    except Exception as e:
        click.echo(f'Error deleting book: {e}')

@cli.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    try:
        Author.create(name)
        click.echo(f'Author "{name}" added.')
    except Exception as e:
        click.echo(f'Error adding author: {e}')

@cli.command()
def view_authors():
    """View all authors."""
    try:
        authors = Author.get_all()
        for author in authors:
            click.echo(f'ID: {author[0]}, Name: {author[1]}')
    except Exception as e:
        click.echo(f'Error fetching authors: {e}')

@cli.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    """Delete an author."""
    try:
        Author.delete(author_id)
        click.echo(f'Author ID {author_id} deleted.')
    except Exception as e:
        click.echo(f'Error deleting author: {e}')

@cli.command()
@click.argument('name')
def add_category(name):
    """Add a new category."""
    try:
        Category.create(name)
        click.echo(f'Category "{name}" added.')
    except Exception as e:
        click.echo(f'Error adding category: {e}')

@cli.command()
def view_categories():
    """View all categories."""
    try:
        categories = Category.get_all()
        for category in categories:
            click.echo(f'ID: {category[0]}, Name: {category[1]}')
    except Exception as e:
        click.echo(f'Error fetching categories: {e}')

@cli.command()
@click.argument('category_id', type=int)
def delete_category(category_id):
    """Delete a category."""
    try:
        Category.delete(category_id)
        click.echo(f'Category ID {category_id} deleted.')
    except Exception as e:
        click.echo(f'Error deleting category: {e}')

if __name__ == '__main__':
    cli()
