
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    author_name TEXT,
    author_email TEXT
);

CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_title TEXT,
    book_description TEXT,
    author_id INTEGER REFERENCES author(author_id),
    genre_id INTEGER REFERENCES genre(genre_id)
);