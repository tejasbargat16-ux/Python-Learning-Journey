# Day 16: Object-Oriented Programming (OOP) Part 3 — Encapsulation & Properties 🔒

## 1. Overview
Encapsulation is the bundling of data (attributes) and methods that operate on that data into a single unit (class), while restricting direct outside access to internal object components to maintain data integrity.

---

## 2. Access Modifiers by Convention in Python
Unlike C++ or Java, Python does not have strict compiler-enforced `public`, `protected`, and `private` keywords. Instead, it relies on naming conventions:

| Modifier | Naming Convention | Example | Accessibility |
|---|---|---|---|
| **Public** | `attribute` | `self.name` | Accessible from anywhere |
| **Protected** | `_attribute` | `self._price` | Internal use warning (by convention, subclasses & class) |
| **Private** | `__attribute` | `self.__balance` | Triggers Name Mangling (`_ClassName__attribute`) |

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._tier = "Silver"       # Protected (convention)
        self.__balance = balance    # Private (mangled to _Account__balance)

acc = Account("Tejas", 5000)
# acc.__balance  -> AttributeError: 'Account' object has no attribute '__balance'
print(acc._Account__balance)  # 5000 (accessible via mangled name, but discouraged)
```

---

## 3. The `@property` Decorator (Pythonic Getters & Setters)
The `@property` decorator allows class methods to be accessed just like regular attributes while enabling validation, encapsulation, and computed fields:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Invokes the @price.setter

    # Getter: called when reading 'product.price'
    @property
    def price(self):
        return self._price

    # Setter: called when assigning 'product.price = value'
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative!")

    # Deleter (optional): called when 'del product.price' is used
    @price.deleter
    def price(self):
        print("Deleting price attribute")
        del self._price
```

### Usage:
```python
item = Product("Mechanical Keyboard", 1500)
print(item.price)    # Accesses getter -> 1500

item.price = 1800    # Accesses setter
# item.price = -100  # Raises ValueError: Price cannot be negative!
```

---

## 4. Why Use `@property` Over Traditional Getters/Setters?
1. **Backwards Compatibility**: Start with plain public attributes (`self.price`). If validation is later needed, convert to `@property` without breaking any existing client code (`obj.price` syntax remains unchanged instead of forcing `obj.get_price()`).
2. **Data Integrity & Validation**: Rejects invalid states immediately at the assignment boundary.
3. **Computed / Read-Only Attributes**: Easily create attributes derived dynamically from other fields without storing duplicate data:
   ```python
   class Circle:
       def __init__(self, radius):
           self.radius = radius

       @property
       def diameter(self):
           return self.radius * 2
   ```

