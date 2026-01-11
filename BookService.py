import csv

class BookService:
    def __init__(self, database):
        self.database = database


    def get_statistics(self):

        books = self.database.get_all_books()
        if not books:
            return None

        total_books = len(books)

        total_price = sum(book.price for book in books)
        avg_price = round(total_price / total_books,2)



        ratings = {}
        for book in books:
            if book.rating in ratings:
                ratings[book.rating] += 1
            else:
                ratings[book.rating] = 1

        ratings_with_percent = {}
        for rating, count in ratings.items():
            percent = (count / total_books) * 100
            ratings_with_percent[rating] = {
                'count': count,
                'percent': round(percent, 2)
            }

        top_category = self.database.get_top_category_by_rating()
        return {
            'total_books': total_books,
            'avg_price': avg_price,
            'ratings': ratings_with_percent,
            'top_category': top_category
        }


    def search_books(self, query):
        all_books = self.database.get_all_books()

        query_lower = query.lower()
        matching_books = []
        for book in all_books:
            if query_lower in book.title.lower():
                matching_books.append(book)

        return matching_books


    def get_category_analysis(self):
        stats = self.database.get_stats_by_category()
        analysis = []
        for row in stats:
            category_data = {
                'category': row[0],
                'book_count': row[1],
                'avg_price': row[2],
                'min_price': row[3],
                'max_price': row[4]
            }
            analysis.append(category_data)
        return analysis

    def export_to_csv(self, filename="books_export.csv"):
        books = self.database.get_all_books()

        if not books:
            return 0

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Category', 'Price', 'Rating', 'Availability', 'URL'])

                for book in books:
                    writer.writerow([
                        book.title,
                        book.category,
                        book.price,
                        book.rating,
                        book.availab,
                        book.url
                        ])
            return len(books)

        except Exception as e:
            return f"Error exporting to CSV: {e}"

