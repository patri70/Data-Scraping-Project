import requests
from bs4 import BeautifulSoup
from Book import Book

class BookScraper:

    def __init__(self):
        self.base_url = "http://books.toscrape.com/"

    def get_categories(self):
        url = requests.get(self.base_url).text
        soup = BeautifulSoup(url, 'html.parser')

        categories = {}
        menu = soup.find('ul', class_ = 'nav nav-list')
        category_list = menu.find('ul')

        for category in category_list.find_all('li'):
            a = category.find('a')
            cat_name = a.text.strip()
            cat_url = self.base_url + a['href']
            categories[cat_name] = cat_url

        return categories

    @staticmethod
    def scrape_category_page(category_url, category_name):
            response = requests.get(category_url)

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

                book = Book(title, category_name, price, rating, availab, url)

                books.append(book)

            return books

    def scrape_category(self, category_url, category_name):
        books = []
        page = 1

        while True:
            if page == 1:
                url = category_url
            else:
                url = category_url.replace('index.html', f'page-{page}.html')

            page_books = self.scrape_category_page(url, category_name)

            if not page_books:
                break
            books.extend(page_books)
            page += 1

        return books

