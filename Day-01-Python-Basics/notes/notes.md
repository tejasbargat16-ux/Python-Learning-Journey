# Day 01: Python Basics — Study Notes 🐍

## 1. Introduction to Python
- Python is a high-level, interpreted, general-purpose programming language.
- Key features:
  - **Readability**: Clean syntax that emphasizes plain-English clarity.
  - **Dynamically Typed**: Variable types do not need explicit declaration; types are bound at runtime.
  - **Memory Management**: Automatic garbage collection and dynamic allocation.
  - **Cross-Platform**: Runs seamlessly on Windows, Linux, macOS, Android (via Termux), etc.

---

## 2. Comments in Python
Comments explain code logic and are ignored by the Python interpreter.

```python
# Single-line comment begins with a hash symbol

"""
Multi-line comments or docstrings are enclosed 
within triple single or double quotes.
"""
```

---

## 3. Variables & Dynamic Typing
- A variable is a named reference pointing to an object in memory.
- Python variables do not store values directly; they store memory references.
- Identifiers must begin with a letter or underscore `_`, followed by letters, digits, or underscores.
- Keywords (e.g., `for`, `def`, `class`, `if`) cannot be used as variable names.

```python
name = "Tejas"      # str
age = 20            # int
cgpa = 8.75         # float
is_student = True   # bool
```

---

## 4. Fundamental Data Types
| Data Type | Description | Example |
|---|---|---|
| `int` | Arbitrary-precision integers | `42`, `-10`, `1000000` |
| `float` | Double-precision floating point numbers | `3.14159`, `-0.5` |
| `str` | Immutable Unicode character sequence | `"Hello"`, `'Python'` |
| `bool` | Boolean truth values | `True`, `False` |
| `NoneType`| Absence of a value / null object | `None` |

```python
x = 10
print(type(x))  # <class 'int'>
```

---

## 5. Input and Output (I/O)
- `print(*objects, sep=' ', end='\n')`: Displays text to standard output.
- `input(prompt)`: Pauses execution and reads a line from standard input as a **string** (`str`).

```python
# Output with custom separators and endings
print("Python", "Learning", "Journey", sep=" - ", end="!\n")

# Reading user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # Must convert str to int
```

---

## 6. Type Conversion (Type Casting)
1. **Implicit Type Conversion**: Done automatically by Python without data loss.
   ```python
   num_int = 10
   num_float = 2.5
   result = num_int + num_float  # Automatically converted to float 12.5
   ```
2. **Explicit Type Conversion (Casting)**: Manually converting using built-in functions:
   - `int(value)`: Converts to integer (truncates floats towards zero).
   - `float(value)`: Converts to floating-point number.
   - `str(value)`: Converts any object into its string representation.
   - `bool(value)`: Evaluates truthiness (`0`, `""`, `None`, `[]` become `False`; others `True`).

---

## 7. Common Pitfalls & Tips
- `input()` **always returns `str`**: Forgetting to cast before mathematical operations causes `TypeError` or unintended string concatenation (`"5" + "5" = "55"`).
- Case Sensitivity: `age`, `Age`, and `AGE` are three completely different variables.
- Division behavior: `/` always returns a `float` in Python 3 (`4 / 2 = 2.0`). For integer division, use `//`.

