from Scraper import BookScraper
from DataBase import BookDatabase
from BookService import BookService
from texttable import Texttable
from concurrent.futures import ThreadPoolExecutor
import threading
db_lock = threading.Lock()

def show_menu():
    print("             Menu:           ")
    print("1. Scrape books from website")
    print("2. Show statistics")
    print("3. Search books by title")
    print("4. Category analysis")
    print("5. Export to CSV")
    print("6. Exit")


def main():
    db = BookDatabase()
    scraper = BookScraper()
    service = BookService(db)

    print("Book Catalog & Analytics System\n")

    while True:
        show_menu()
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            with db_lock:
                db.clear_database()

            categories = scraper.get_categories()
            selected_categories = list(categories.items())[:13]

            results = []
            with ThreadPoolExecutor(max_workers=4) as executor:
                for category_info in selected_categories:
                    result = executor.submit(scrape_save, category_info, scraper, db)
                    results.append(result)

            total_saved = 0
            for future in results:
                total_saved += future.result()

            print(f"Scraping completed. Total books saved: {total_saved}\n")

        elif choice == 2:
            # Statistics
            stats = service.get_statistics()
            try:
                print("Catalog Statistics:")
                print(f"Total Books: {stats['total_books']}")
                print(f"Average Price: £{float(stats['avg_price'])}")
                print()
                print("Top 5-Star Category:", stats['top_category'][0], "(", stats['top_category'][1], "books)")
                print("Ratings Distribution:")
                for rating, data in stats['ratings'].items():
                    print(f"  {rating} stars: {data['count']} books ({data['percent']}%)")
                print()
            except Exception:
                print("No statistics available. Please scrape books first.\n")

        elif choice == 3:
            # Search books
            query = input("Enter search term (book title): ").strip()

            if query:
                books = service.search_books(query)
                if books:
                    print(f"Search Results for '{query}'")
                    display_table(books)
                else:
                    print(f"No books found matching '{query}'")
            else:
                print("Please enter a search term.")

        elif choice == 4:
            print("Category Analysis (Sorted by Average Price):")
            stats = service.get_category_analysis()

            if stats:
                table = Texttable()
                table.set_cols_align(["l", "r", "r", "r"])
                table.set_cols_width([30, 10, 15, 15])
                table.header(["Category", "Book Count", "Avg Price", "Range (Min-Max)"])

                for item in stats:
                    price_range = f"£{item['min_price']} - £{item['max_price']}"
                    table.add_row([
                        item['category'],
                        item['book_count'],
                        f"£{round(float(item['avg_price']),2)}",
                        price_range
                    ])

                print(table.draw())
            else:
                print("No category data available. Please scrape books first.\n")

        elif choice == 5:
            # Export to CSV
            num_exported = service.export_to_csv()
            if num_exported > 0:
                print(f"Exported {num_exported} books to books_export.csv")
            else:
                print("No books to export or error occurred.")

        elif choice == 6:
            # Exit
            print("Goodbye!")
            db.close()
            break
            

        else:
            print("Invalid choice. Please try again.\n")


def display_table(books):
    table = Texttable()

    table.set_cols_align(["l", "r", "c"])
    table.set_cols_width([50, 10, 10])
    table.header(["Title", "Price", "Rating"])

    for book in books:
        table.add_row([book.title, f"{round(float(book.price),2)}£", book.rating])

    print(table.draw())

def scrape_save(category_info, scraper, db):
    category_name, category_url = category_info
    books = scraper.scrape_category(category_url, category_name)

    if books:
        with db_lock:
            saved = db.save_books(books)
            print(f"  Saved {saved} books from {category_name}\n")
        return saved

    return 0


if __name__ == "__main__":
    main()
