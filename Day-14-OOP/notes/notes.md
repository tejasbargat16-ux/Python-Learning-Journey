# Day 14: Object-Oriented Programming (OOP) Part 1 — Study Notes 🏛️

## 1. Overview
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **data (objects)** and **behavior (methods)** rather than functions and logic alone.

---

## 2. Core Concepts: Classes and Objects

- **Class**: A blueprint or prototype from which objects are created.
- **Object (Instance)**: A concrete realization or instance of a class occupying distinct memory space.

```python
class Student:
    """Blueprint for creating Student objects."""
    pass

# Creating an instance of Student
s1 = Student()
```

---

## 3. The `__init__` Method & `self`

### 3.1 Constructor (`__init__`)
A special dunder (double underscore) method automatically called when a new instance is instantiated to initialize its state.

### 3.2 The `self` Parameter
- Represents the instance currently calling the method.
- Provides access to the attributes and methods of that specific object.
- Must be the first parameter of any instance method in Python (passed implicitly at call time).

```python
class Student:
    def __init__(self, name, roll_number, marks):
        # Instance attributes
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name} | Roll No: {self.roll_number} | Marks: {self.marks}")

s1 = Student("Tejas", 101, 92)
s1.display_details()
```

---

## 4. Class Attributes vs Instance Attributes

| Feature | Instance Attribute | Class Attribute |
|---|---|---|
| **Definition** | Inside `__init__` via `self.attribute` | Inside class body directly outside any method |
| **Scope** | Unique to each individual object | Shared by all instances of the class |
| **Modification** | Changing on one instance does not affect others | Modifying via `ClassName.attr` affects all instances |

```python
class Employee:
    company_name = "Tech Corp"  # Class attribute

    def __init__(self, name, salary):
        self.name = name        # Instance attribute
        self.salary = salary    # Instance attribute

e1 = Employee("Alice", 70000)
e2 = Employee("Bob", 80000)

print(e1.company_name)  # "Tech Corp"
print(e2.company_name)  # "Tech Corp"
```

---

## 5. Instance Methods
Functions defined inside a class that take `self` as their first parameter. They can read and modify the object's instance state.

```python
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        raise ValueError("Insufficient balance or invalid amount.")
```

