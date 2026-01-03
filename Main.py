from Scraper import BookScraper
from DataBase import BookDatabase
from BookService import BookService
from UI import UI
import time


def main():
    db = BookDatabase()
    scraper = BookScraper()
    service = BookService(db)
    ui = UI()

    while True:
        ui.show_menu()
        choice = ui.get_menu_choice()

        if choice == '1':
            # Scraping
            ui.show_info("\nScraping first 5 pages (~100 books)...")
            books = []

            for page in range(1, 6):
                ui.show_scraping_progress(page, 5)
                page_books = scraper.scrape_page(page)
                if not page_books:
                    break
                books.extend(page_books)
                time.sleep(0.1)

            if books:
                num_saved = db.save_books(books)
                ui.show_success(f"Successfully scraped and saved {num_saved} books!\n")
            else:
                ui.show_error("No books found.\n")

        elif choice == '2':
            # Statistics
            stats = service.get_statistics()
            ui.show_statistics(stats)

        elif choice == '3':
            # Search books
            query = ui.get_search_query()

            if query:
                books = service.search_books(query)
                if books:
                    ui.display_books_table(books, f"Search Results for '{query}'")
                else:
                    ui.show_info(f"No books found matching '{query}'")
            else:
                ui.show_error("Please enter a search term.")

        elif choice == '4':
            # Cheapest books
            books = service.find_cheapest_books(10)
            ui.display_books_table(books, "Top 10 Cheapest Books")

        elif choice == '5':
            # Highest rated books
            books = service.find_highest_rated(10)
            ui.display_books_table(books, "Top 10 Highest Rated Books")

        elif choice == '6':
            # Export to CSV
            num_exported = service.export_to_csv()
            if num_exported > 0:
                ui.show_success(f"Exported {num_exported} books to books_export.csv")
            else:
                ui.show_error("No books to export or error occurred.")

        elif choice == '7':
            # Exit
            ui.show_success("\nGoodbye!")
            db.close()
            break

        else:
            ui.show_error("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
