class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_details(self):
        self.display_brand()
        print("Model:", self.model)


car1 = Car("Toyota", "Innova")

car1.display_details()

