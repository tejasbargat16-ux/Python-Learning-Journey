class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price!")

    def display(self):
        print("Product:", self.name)
        print("Price: ₹", self.price)


product1 = Product("Keyboard", 800)

product1.display()

product1.price = 1000

print("\nAfter updating price:")
product1.display()

product1.price = -500

print("\nAfter invalid update:")
product1.display()
