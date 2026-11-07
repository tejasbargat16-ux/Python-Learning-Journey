# Day 11: Exception Handling in Python — Study Notes 🛡️

## 1. Overview
An **exception** is an error that occurs during program execution that disrupts the normal flow of instructions. Exception handling prevents abrupt crashes and allows programs to gracefully recover or report helpful diagnostics.

---

## 2. Syntax & Blocks: `try`, `except`, `else`, `finally`

```python
try:
    # 1. Critical code that might raise an exception
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
except ValueError:
    # 2. Handled if input is not a valid integer
    print("Error: Input must be a valid integer.")
except ZeroDivisionError:
    # 3. Handled if denominator is 0
    print("Error: Division by zero is undefined.")
except Exception as e:
    # 4. Catches any other standard exception
    print(f"Unexpected error: {e}")
else:
    # 5. Executes ONLY if no exception was raised in try block
    print(f"Success! Result = {result}")
finally:
    # 6. ALWAYS executes, regardless of whether exceptions occurred or were caught
    print("Cleanup: Operation complete.")
```

---

## 3. Catching Multiple Exceptions
Exceptions can be grouped in a single `except` tuple:

```python
try:
    data = [10, 20, 30]
    val = data[int(input("Enter index: "))]
except (IndexError, ValueError) as err:
    print(f"Invalid access: {err}")
```

---

## 4. The `raise` Keyword
Used to intentionally trigger an exception when business rules or preconditions are violated:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 18:
        raise PermissionError("Access restricted to users aged 18+.")
    return "Access granted"

try:
    check_age(-5)
except ValueError as ex:
    print(f"Validation failed: {ex}")
```

---

## 5. Built-in Exceptions Hierarchy
All built-in exceptions inherit from `BaseException` (and typically `Exception`):
- `ZeroDivisionError`: Division or modulo by zero.
- `ValueError`: Function receives an argument of right type but invalid value (`int("abc")`).
- `TypeError`: Operation applied to an incompatible data type (`"5" + 2`).
- `IndexError`: Sequence subscript out of range.
- `KeyError`: Dictionary key not found.
- `FileNotFoundError`: File path does not exist.
- `NameError`: Local or global name is not defined.

---

## 6. Best Practices
1. **Never use bare `except:`**: Catching all exceptions blindly (without naming the exception) catches keyboard interrupts (`Ctrl+C`) and system exits. Always catch specific exceptions (`except ValueError:`).
2. **Keep `try` blocks small**: Place only the line that might fail inside `try`, keeping business logic in `else`.
3. **Use `finally` for resource cleanup**: Ensure files, network sockets, or database connections close properly.

