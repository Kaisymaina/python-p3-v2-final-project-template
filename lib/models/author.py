from config.connection import CONN, CURSOR

class Author:
    def __init__(self, author_id, author_name, author_email):
        self.author_id = author_id
        self.author_name = author_name
        self.author_email = author_email
    @classmethod
    def drop_table(cls):
        sql="""DROP TABLE IF EXISTS author"""
        CURSOR.execute(sql)
        CONN.commit()
        

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE author (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_name TEXT,
            author_email TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO author (
            author_name,
            author_email
        ) VALUES (?, ?)
        """
        CURSOR.execute(
            sql, (
                self.author_name,
                self.author_email
            )
        )
        CONN.commit()
        self.id = CURSOR.lastrowid


            
        

    