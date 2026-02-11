# 📚 Data Scraping Project

This project is a Python application that scrapes book data from a website and stores it in a local database.
It was built as a learning project to practice web scraping, object-oriented programming, and database interaction in Python.

---

## 🚀 What This Project Does

- Scrapes book information (title, price, rating, availability, genre)
- Uses multi-threading for faster data collection
- Structures the data using a dedicated Book model
- Saves the extracted data into a local SQLite database
- Calculates statistics and exports data to CSV

The main goal of this project was to better understand:
- Web scraping with requests and BeautifulSoup
- OOP principles in Python
- Database handling with SQLite
- Concurrency and Thread Safety

---

## 🗂️ Project Structure

```
Data-Scraping-Project/
│
├── Book.py          # Defines the Book model
├── BookService.py   # Contains business logic and statistics
├── DataBase.py      # Manages database connection and operations
├── Scraper.py       # Contains scraping logic
├── Main.py          # Entry point (menu and threading)
└── README.md
```
---

## ⚙️ Technologies Used

- Python 3
- requests
- BeautifulSoup
- SQLite
- texttable

---

## 💻 How to Run the Project

1. Clone the repository:

    git clone https://github.com/patri70/Data-Scraping-Project.git
    cd Data-Scraping-Project

2. Install dependencies:

    pip install requests beautifulsoup4 texttable

3. Run the application:

    python Main.py

---

## 🧠 How It Works

- **Scraper.py** extracts data from the target website.
- **Book.py** defines the structure of a book object.
- **BookService.py** processes statistics and search logic.
- **DataBase.py** handles saving and retrieving data from SQLite.
- **Main.py** connects everything together and manages the user menu.

---

## 🎯 Purpose

This project was created as a learning exercise to strengthen my understanding of:

- Object-Oriented Programming
- Python backend fundamentals
- Clean project structure
- Preparing for software engineering internships

---

## 📜 License

This project is for educational purposes.
