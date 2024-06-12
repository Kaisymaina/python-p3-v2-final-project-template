--creating author table
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    author_name TEXT,
    author_email TEXT
);

--creating books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_title TEXT,
    book_description TEXT,
    author_id INTEGER REFERENCES author(author_id),
    genre_id INTEGER REFERENCES genre(genre_id)
);

--creating genre table
CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT
);



--inserting data into table author
INSERT INTO author (author_id, author_name, author_email) 
VALUES 
(1, 'J.K Rowling', 'rowlingsK@gmail.com'),
(2, 'George R.R Martin', 'georgemartin@gmail.com'),
(3, 'Stephen King', 'stephenking@gmail.com'),
(4, 'Margaret Atwood', 'margaretatwood@gmail.com'),
(5, 'Haruki Murakami', 'harukimurakami@gmail.com');


--inserting data into table books
INSERT INTO books (book_id, book_title, book_description, author_id) 
VALUES 
(1, 'Norwegian Wood', 'Melancholic tale of love and loss.', 5),
(2, 'Harry Potter', 'Young wizards adventures at magical school.', 1),
(3, 'The Handmaids Tale', 'Dystopian future where women are subjugated.', 4),
(4, 'IT', 'Terrifying shape-shifting clown haunts small town.', 3),
(5, 'A Song of Ice and Fire', 'Epic fantasy of power, betrayal, and dragons.', 2),
(6, 'Oryx and Crake','Dystopian tale of genetic engineering gone wrong.', 4),
(7, 'Kafka on the Shore', 'Surreal exploration of identity and human connection.', 5),
(8, 'The Shining', 'Family trapped in haunted hotels dark past.', 3),
(9, 'Game of Thrones', 'Epic fantasy of power struggles and royal intrigue.', 2),



--insterting data into genre
INSERT INTO genre (genre_id, genre_name, book_id ) 
VALUES 
(1, 'Dark Fantasy' 5),
(2, 'Young Adult' 2),
(3, 'Epic Fantasy' 5),
(4, 'Romance' 1),
(5, 'Speculative Fiction' 3),
(6, 'Horror' 4),
(7, 'Science Fiction' 3),
(8, 'Literary Fiction'1 ),
(9, 'Fantasy' 2),
(10, 'Coming-of-Age'1 ),
(11, 'Thriller' 4),
(12, 'Dystopian' 3);