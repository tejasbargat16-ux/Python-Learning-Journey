# Day 03: Conditional Statements in Python — Study Notes 🔀

## 1. Overview
Conditional statements allow a program to execute different blocks of code depending on whether a given boolean expression evaluates to `True` or `False`.

In Python, indentation (typically 4 spaces) defines the block scope instead of curly braces `{}`.

---

## 2. Forms of Conditional Statements

### 2.1 The `if` Statement
Executes a block of code only when the condition is `True`.

```python
score = 85
if score >= 40:
    print("Pass")
```

### 2.2 The `if-else` Statement
Provides an alternative block to execute when the condition is `False`.

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 2.3 The `if-elif-else` Ladder
Evaluates multiple sequential conditions. As soon as one condition evaluates to `True`, its block executes and the rest of the ladder is skipped.

```python
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")
```

### 2.4 Nested `if` Statements
An `if` statement placed inside another `if` or `else` block to check multi-tier conditions.

```python
age = 19
has_id = True

if age >= 18:
    if has_id:
        print("Access granted.")
    else:
        print("Please present a valid ID.")
else:
    print("Underage. Access denied.")
```

---

## 3. The Ternary Operator (Conditional Expression)
A concise one-line syntax for simple `if-else` assignments:

$$\text{value\_if\_true} \quad \mathbf{if} \quad \text{condition} \quad \mathbf{else} \quad \text{value\_if\_false}$$

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## 4. Truthy and Falsy Values
In Python, expressions in conditions do not have to be strictly booleans; every object has a boolean value:

| Falsy Values (evaluate to `False`) | Truthy Values (evaluate to `True`) |
|---|---|
| Constants: `None`, `False` | Any non-zero number: `1`, `-5`, `3.14` |
| Zero numbers: `0`, `0.0`, `0j` | Non-empty strings: `"hello"`, `" "` |
| Empty sequences: `""`, `[]`, `()`, `range(0)` | Non-empty collections: `[1]`, `{"k": "v"}` |
| Empty mappings: `{}` | Custom objects (unless `__bool__` returns `False`) |

```python
cart = []
if not cart:
    print("Your shopping cart is empty!")
```

---

## 5. Best Practices & Pitfalls
- **Avoid redundant comparisons**: Write `if is_valid:` instead of `if is_valid == True:`.
- **Chained comparisons**: Python allows clean mathematical ranges:
  ```python
  if 10 <= x <= 50:
      print("x is within range [10, 50]")
  ```
- **Consistent indentation**: Never mix tabs and spaces (PEP 8 standard is 4 spaces).

