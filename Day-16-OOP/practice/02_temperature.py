class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            print("Temperature cannot be below absolute zero!")

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


temp1 = Temperature(25)

print("Celsius:", temp1.celsius)
print("Fahrenheit:", temp1.fahrenheit)

temp1.celsius = 100

print("\nUpdated Celsius:", temp1.celsius)
print("Updated Fahrenheit:", temp1.fahrenheit)
