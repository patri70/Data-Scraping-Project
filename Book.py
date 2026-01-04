class Book:
    def __init__(self, title, price, rating, availab, url):
        self.title = title
        self.price = price
        self.rating = rating
        self.availab = availab
        self.url = url

    def rating_num(self):
        ratings_map = { 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5 }
        return ratings_map[self.rating]

    def __str__(self):
        return f"{self.title} - £{self.price} - rating {self.rating} - {self.availab}"
