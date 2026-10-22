class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: ₹", self.price)


mobile1 = Mobile("Samsung", "A16", 15000)
mobile2 = Mobile("Redmi", "Note 13", 18000)

print("--- Mobile 1 ---")
mobile1.display()

print("\n--- Mobile 2 ---")
mobile2.display()
