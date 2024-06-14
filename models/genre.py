from orm.orm import ORM

class Genre:
    orm = ORM('library.db')

    @classmethod
    def create(cls, name):
        try:
            cls.orm.execute('INSERT INTO genres (name) VALUES (?)', (name,))
            print("Genre created successfully.")
        except Exception as e:
            print(f"Error creating genre: {e}")

    @classmethod
    def get_all(cls):
        try:
            genres = cls.orm.fetchall('SELECT * FROM genres')
            return genres
        except Exception as e:
            print(f"Error fetching genres: {e}")
            return []

    @classmethod
    def delete(cls, genre_id):
        try:
            cls.orm.execute('DELETE FROM genres WHERE id = ?', (genre_id,))
            print("Genre deleted successfully.")
        except Exception as e:
            print(f"Error deleting genre: {e}")
