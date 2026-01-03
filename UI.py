from rich.console import Console
from rich.table import Table

class UI:
    def __init__(self):
        self.console = Console()

    def show_statistics(self, stats):
        if not stats:
            self.console.print("[yellow]No books in database. Please scrape first.[/yellow]")
            return

        self.console.print("\n[bold cyan]Catalog Statistics[/bold cyan]")
        self.console.print(f"Total Books: {stats['total_books']}")
        self.console.print(f"Average Price: {stats['avg_price']:.2f}£")
        self.console.print(f"Cheapest Book: {stats['min_price']:.2f}£")
        self.console.print(f"Most Expensive Book: {stats['max_price']:.2f}£")

        self.console.print("\n[bold cyan]Rating Distribution[/bold cyan]")
        for rating, count in sorted(stats['ratings'].items()):
            self.console.print(f"{rating}: {count} books")

            print()

    def get_search_query(self):
            """Get search query from user"""
            query = input("\nEnter search term (book title): ")
            return query.strip()

    def get_user_choice(self, max_choice):
            """Get user's numeric choice"""
            try:
                choice = input("\nEnter category number to view books: ")
                category_index = int(choice) - 1
                if 0 <= category_index < max_choice:
                    return category_index
                else:
                    self.console.print("[red]Invalid choice.[/red]")
                    return None
            except ValueError:
                self.console.print("[red]Invalid input.[/red]")
                return None

    def display_books_table(self, books, title="Books"):
            """Display books in a formatted table"""
            if not books:
                self.console.print("[yellow]No books found.[/yellow]")
                return

            table = Table(title=title)

            table.add_column("Title", style="cyan", no_wrap=False, max_width=40)
            table.add_column("Price", style="green")
            table.add_column("Rating", style="yellow")
            table.add_column("Availability", style="magenta")

            for book in books:
                table.add_row(
                    book.title,
                    f"£{book.price:.2f}",
                    book.rating,
                    book.availab
                )

            self.console.print(table)
            print()  # blank line

    def show_success(self, message):
            """Display success message"""
            self.console.print(f"[green]{message}[/green]")

    def show_error(self, message):
            """Display error message"""
            self.console.print(f"[red]{message}[/red]")

    def show_info(self, message):
            """Display info message"""
            self.console.print(f"[yellow]{message}[/yellow]")

    def show_menu(self):
            """Display main menu"""
            self.console.print("\n[bold green]Book Catalog & Analytics System[/bold green]\n")
            self.console.print("[bold cyan]Menu:[/bold cyan]")
            print("1. Scrape books from website")
            print("2. Show statistics")
            print("3. Search books by title")
            print("4. Find cheapest books")
            print("5. Find highest rated books")
            print("6. Export to CSV")
            print("7. Exit")

    def get_menu_choice(self):
            """Get user's menu choice"""
            return input("\nEnter your choice (1-7): ")

    def show_scraping_progress(self, page, total_pages):
            """Show scraping progress"""
            self.console.print(f"Scraping page {page}/{total_pages}...")
