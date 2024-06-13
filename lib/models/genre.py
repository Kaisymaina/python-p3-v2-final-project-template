from config.connection import CONN, CURSOR

class Genre:
    def __init__(self, genre_id, genre_name):
        self.genre_id = genre_id
        self.genre_name = genre_name

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS genre"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE genre (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_name TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO genre (
            genre_name
        ) VALUES (?)
        """
        CURSOR.execute(
            sql, (
                self.genre_name,
            )
        )
        CONN.commit()
        self.genre_id = CURSOR.lastrowid

# Example usage
Genre.drop_table()
Genre.create_table()

genre1 = Genre(None, 'Romance')
genre1.save()

genre2 = Genre(None, 'Young Adult')
genre2.save()

genre3 = Genre(None, 'Speculative Fiction')
genre3.save()

genre4 = Genre(None, 'Horror')
genre4.save()

genre5 = Genre(None, 'Epic Fantasy')
genre5.save()

genre6 = Genre(None, 'Literary Fiction')
genre6.save()