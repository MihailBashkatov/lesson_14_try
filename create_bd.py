import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
            DROP TABLE books;
            DROP TABLE books_2;
            DROP TABLE books_3;
            DROP TABLE books_4;
            DROP TABLE books_5;
             
    """

    cursor.executescript(query)