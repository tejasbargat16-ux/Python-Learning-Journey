# Day 15: Object-Oriented Programming (OOP) Part 2 — Study Notes 🧬

## 1. Overview
Day 15 explores the relationship between classes: **Inheritance** (code reuse and establishing an *is-a* relationship) and **Polymorphism** (common interface with diverse underlying behaviors).

---

## 2. Inheritance
A mechanism where a child (derived/subclass) class acquires all methods and properties from a parent (base/superclass) class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} barks!"

d = Dog("Buddy")
print(d.speak())  # "Buddy barks!"
```

---

## 3. Types of Inheritance in Python

1. **Single Inheritance**: Child inherits from one parent class.
   $$\text{Parent} \longrightarrow \text{Child}$$
2. **Multilevel Inheritance**: A child class inherits from another child class.
   $$\text{Grandparent} \longrightarrow \text{Parent} \longrightarrow \text{Child}$$
3. **Multiple Inheritance**: A class inherits directly from more than one base class.
   $$\text{Parent A, Parent B} \longrightarrow \text{Child}$$
4. **Hierarchical Inheritance**: Multiple child classes inherit from a single parent.
   $$\text{Parent} \longrightarrow \text{Child 1, Child 2}$$

---

## 4. The `super()` Function
Used to call the constructor or methods of the parent superclass without explicitly naming the parent class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call parent constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
```

---

## 5. Method Overriding
When a subclass provides a specific implementation of a method that is already defined in its parent class.

```python
class Vehicle:
    def fuel_type(self):
        return "Generic Fuel"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric Battery (kWh)"  # Overridden behavior
```

---

## 6. Polymorphism (Duck Typing & Method Overriding)
Polymorphism allows different classes to implement methods with the same name, enabling interchangeable use:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# Uniform interface:
shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"Area: {s.area():.2f}")
```
> *"If it walks like a duck and quacks like a duck, it's a duck." (Python's Duck Typing philosophy)*

