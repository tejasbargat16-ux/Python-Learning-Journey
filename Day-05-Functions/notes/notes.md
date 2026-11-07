# Day 05: Functions in Python — Study Notes ⚙️

## 1. Overview
A function is a reusable, self-contained block of organized code designed to perform a single coherent action. Functions promote the **DRY (Don't Repeat Yourself)** principle and make code modular and testable.

---

## 2. Defining & Calling Functions
- Defined using the `def` keyword.
- Parameters define the expected inputs in the function signature.
- Arguments are the concrete values passed during the function call.

```python
def greet(name):  # 'name' is a parameter
    """Docstring explaining the purpose of greet."""
    return f"Hello, {name}!"

message = greet("Tejas")  # "Tejas" is an argument
print(message)
```

---

## 3. Function Arguments Types

### 3.1 Positional Arguments
Arguments matched by position and order:
```python
def add(a, b):
    return a + b

print(add(10, 20))  # a=10, b=20
```

### 3.2 Keyword Arguments
Explicitly identifying parameters by name during call time:
```python
print(add(b=20, a=10))  # Order does not matter
```

### 3.3 Default Parameters
Parameters that assume a default fallback value if omitted in the function call:
```python
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_user("Tejas"))            # Hello, Tejas!
print(greet_user("Amit", "Welcome"))  # Welcome, Amit!
```
> [!WARNING]
> Default arguments must always follow non-default positional arguments in the signature.

---

## 4. Return Statements
- `return` sends a result back to the caller and terminates function execution immediately.
- Functions without an explicit `return` statement return `None` by default.
- Multiple values can be returned as a tuple:
  ```python
  def min_max(numbers):
      return min(numbers), max(numbers)  # Returns a tuple

  low, high = min_max([4, 1, 9, 2])
  ```

---

## 5. Variable Scope & Lifetime (LEGB Rule)
Python resolves names using the **LEGB** hierarchy:
1. **L**ocal: Inside current function.
2. **E**nclosing: In any outer enclosing functions (closures).
3. **G**lobal: At the top level of the module file.
4. **B**uilt-in: Python standard namespace (`len`, `range`, `print`).

```python
count = 10  # Global variable

def update():
    global count  # Required to modify global scope directly
    count += 1

update()
print(count)  # 11
```

---

## 6. Lambda Functions (Anonymous Functions)
Small, single-expression anonymous functions defined with the `lambda` keyword:

$$\lambda \quad \text{arguments} : \text{expression}$$

```python
square = lambda x: x ** 2
print(square(5))  # 25

# Frequently used as sorting keys
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda item: item[0])
```

---

## 7. Best Practices
- Keep functions small and focused on a single responsibility.
- Use informative names adhering to `snake_case`.
- Always document functions with meaningful docstrings (`"""..."""`).

