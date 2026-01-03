import sqlite3
from Book import Book

class BookDatabase:
    def __init__(self, db_name = "books.db"):
        self.db_name = db_name
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            rating TEXT,
            availab TEXT,
            url TEXT
            )
            ''')

        self.connect.commit()

    def save_books(self, books):
        self.cursor.execute('DELETE FROM books')

        for book in books:
            self.cursor.execute('''
                INSERT INTO books (title, price, rating, availab, url)
                VALUES (?, ?, ?, ?, ?)
            ''', (book.title, book.price, book.rating, book.availab, book.url))

        self.connect.commit()
        return len(books)

    def get_all_books(self):

        self.cursor.execute('SELECT title, price, rating, availab, url FROM books')
        rows = self.cursor.fetchall()

        books = []
        for row in rows:
            book = Book(row[0], row[1], row[2], row[3], row[4])
            books.append(book)

        return books

    def close(self):
        self.connect.close()