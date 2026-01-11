from Scraper import BookScraper
from DataBase import BookDatabase
from BookService import BookService
from texttable import Texttable
import time


def show_menu():
    print("             Menu:           ")
    print("1. Scrape books from website")
    print("2. Show statistics")
    print("3. Search books by title")
    print("4. Find cheapest books with high ratings")
    print("5. Export to CSV")
    print("7. Exit")


def main():
    db = BookDatabase()
    scraper = BookScraper()
    service = BookService(db)

    print("Book Catalog & Analytics System\n")

    while True:
        show_menu()
        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            print("Scraping first 7 categories...\n")
            db.clear_database()

            categories = scraper.get_categories()
            selected_categories = list(categories.items())[:7]
            total_saved = 0

            for category_name, category_url in selected_categories:
                print(f"Scraping category: {category_name}...")
                books = scraper.scrape_category(category_url, category_name)

                if books:
                    saved = db.save_books(books)
                    total_saved += saved
                    print(f"  Saved {saved} books from {category_name}\n")
                else:
                    print(f"  No books found in {category_name}\n")
                time.sleep(2)

            print(f"Scraping completed. Total books saved: {total_saved}\n")

        elif choice == 2:
            # Statistics
            stats = service.get_statistics()
            try:
                print("Catalog Statistics:")
                print(f"Total Books: {stats['total_books']}")
                print(f"Average Price: £{float(stats['avg_price'])}")
                print(f"Minimum Price: £{float(stats['min_price'])}")
                print(f"Maximum Price: £{float(stats['max_price'])}")
                print()
                print("Ratings Distribution:")
                for rating, count in stats['ratings'].items():
                    print(f"  {rating} stars: {count} books")
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
            # Cheapest books
            books = service.cheap_book_high_rating(10)
            print("Top 10 Cheapest Books with High Ratings")
            display_table(books)


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
        table.add_row([book.title, f"£{float(book.price)}£", book.rating])

    print(table.draw())


if __name__ == "__main__":
    main()
