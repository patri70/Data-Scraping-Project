import requests
from bs4 import BeautifulSoup
from Book import Book

class BookScraper:

    def __init__(self):
        self.base_url = "http://books.toscrape.com/catalogue/page-{}.html"

    def scrape_page(self, page_num):
            url = self.base_url.format(page_num)
            response = requests.get(url)

            if response.status_code != 200:
                return []

            soup = BeautifulSoup(response.content, 'html.parser')

            book_elements = soup.find_all('article', class_ = 'product_pod')

            books = []
            for element in book_elements:
                title = element.find('h3').find('a')['title']

                price_text = element.find('p', class_='price_color').text
                price = float(price_text.replace('£', ''))

                rating_element = element.find('p', class_='star-rating')
                rating = rating_element['class'][1] if rating_element else 'Unknown'

                availab = element.find('p', class_='instock availability').text.strip()

                url = element.find('h3').find('a')['href']

                book = Book(title, price, rating, availab, url)

                if book:
                    books.append(book)

            return books


