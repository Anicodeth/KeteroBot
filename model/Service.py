class Service:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Service: {self.name}\nDescription: {self.description}\nPrice: {self.price}"
