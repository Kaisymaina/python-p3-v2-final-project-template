--creating author table
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    author_name TEXT,
    author_email TEXT
);
--creating genre table
CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT
);
--creating books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_title TEXT,
    book_description TEXT,
    author_id INTEGER REFERENCES author(author_id),
    genre_id INTEGER REFERENCES genre(genre_id)
);


--inserting data into table author
INSERT INTO author (author_id, author_name, author_email) 
VALUES 
(1, 'J.K Rowling', 'rowlingsK@gmail.com'),
(2, 'George R.R Martin', 'georgemartin@gmail.com'),
(3, 'Stephen King', 'stephenking@gmail.com'),
(4, 'Margaret Atwood', 'margaretatwood@gmail.com'),
(5, 'Haruki Murakami', 'harukimurakami@gmail.com');


--