class Book:
    def __init__(self, title, price, rating, availab, url):
        self.title = title
        self.price = price
        self.rating = rating
        self.availab = availab
        self.url = url

    def to_dict(self):
        return {
            'title': self.title,
            'price': self.price,
            'rating': self.rating,
            'availab':self.availab,
            'url': self.url
        }

    def __str__(self):
        return f"{self.title} - £{self.price} - rating {self.rating} - {self.availab}"
