class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} cost ${self.price}"

class Equiptment(Product):
    def __init__(self, name, price, weight, sport):
        super().__init__(name, price)
        self.weight = weight
        self.sport = sport
    def __str__(self):
        return f'A {self.sport} {self.name} that weights {self.weight} and cost ${self.product}'

equipment = Equiptment('Bat', 50, 2, 'Baseball')

print (equipment)