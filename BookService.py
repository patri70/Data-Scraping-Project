import csv

class BookService:
    RATING_VALUES = {'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2, 'One': 1}

    def __init__(self, database):
        self.database = database

    def get_statistics(self):

        books = self.database.get_all_books()
        if not books:
            return None

        total_books = len(books)

        total_price = sum(book.price for book in books)
        avg_price = total_price / total_books

        min_price = min(book.price for book in books)
        max_price = max(book.price for book in books)

        ratings = {}
        for book in books:
            if book.rating in ratings:
                ratings[book.rating] += 1
            else:
                ratings[book.rating] = 1

        return {
            'total_books': total_books,
            'avg_price': avg_price,
            'min_price': min_price,
            'max_price': max_price,
            'ratings': ratings
        }

    def search_books(self, query):
        all_books = self.database.get_all_books()

        if not all_books:
            return []

        query_lower = query.lower()
        matching_books = []
        for book in all_books:
            if query_lower in book.title.lower():
                matching_books.append(book)

        return matching_books

    def find_cheapest_books(self, n=10):
        books = self.database.get_all_books()

        if not books:
            return []

        sorted_books = sorted(books, key = lambda b: b.price)

        return sorted_books[:n]

    def find_highest_rated(self, n=10):
        books = self.database.get_all_books()

        if not books:
            return []

        sorted_books = sorted(books, key=lambda book: self.RATING_VALUES.get(book.rating, 0), reverse=True )

        return sorted_books[:n]

    def export_to_csv(self, filename="books_export.csv"):
        books = self.database.get_all_books()

        if not books:
            return 0

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Price', 'Rating', 'Availability', 'URL'])

                for book in books:
                    writer.writerow([
                        book.title,
                        book.price,
                        book.rating,
                        book.availab,
                        book.url
                        ])
            return len(books)

        except Exception as e:
            return f"Error exporting to CSV: {e}"

