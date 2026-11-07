# Day 21: Python Context Managers — Study Notes 🔄

## 1. Overview
A **Context Manager** is a Python construct that simplifies resource management by ensuring setup and cleanup actions are reliably executed around a block of code, even if unhandled exceptions or crashes occur.

The most common example is handling files with the `with` statement:
```python
with open("data.txt", "r") as f:
    content = f.read()
# File is guaranteed to be closed here automatically
```

---

## 2. The Context Management Protocol: `__enter__` and `__exit__`

Any Python class can become a context manager by implementing two special dunder methods:

1. `__enter__(self)`:
   - Sets up the resource (e.g., opens a connection, starts a timer).
   - The value it returns is bound to the target variable after the `as` keyword in `with ... as var:`.
2. `__exit__(self, exc_type, exc_val, exc_tb)`:
   - Cleans up the resource (e.g., closes files, stops timers, rolls back database transactions).
   - Receives exception details if an error occurred inside the `with` block:
     - `exc_type`: Exception class (e.g., `ZeroDivisionError`) or `None`.
     - `exc_val`: Exception instance with error message or `None`.
     - `exc_tb`: Traceback object or `None`.
   - **Exception Suppression**: If `__exit__` returns `True`, Python **suppresses** the exception and continues execution normally. If it returns `False` or `None`, the exception is re-raised.

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")
        return False  # Do not suppress exceptions

with Timer():
    total = sum(i**2 for i in range(100_000))
```

---

## 3. Exception Handling in `__exit__`

```python
class IgnoreErrors:
    def __init__(self, *exceptions_to_ignore):
        self.exceptions = exceptions_to_ignore

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions):
            print(f"Suppressed exception: {exc_val}")
            return True  # Suppress!
        return False     # Propagate other exceptions

with IgnoreErrors(ZeroDivisionError):
    result = 10 / 0  # Does not crash!

print("Program continues smoothly...")
```

---

## 4. Generator-Based Context Managers: `@contextlib.contextmanager`
Instead of writing a full class with `__enter__` and `__exit__`, you can write a generator function decorated with `@contextmanager`:
- Everything before `yield` acts as `__enter__`.
- The value yielded is passed to the `as` variable.
- Everything inside `finally` after `yield` acts as `__exit__`.

```python
from contextlib import contextmanager
import time

@contextmanager
def execution_timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"[{label}] Execution took: {end - start:.4f}s")

with execution_timer("Calculation"):
    _ = [x**2 for x in range(500_000)]
```

---

## 5. Built-in Utilities in `contextlib`

### 5.1 `contextlib.suppress(*exceptions)`
Ignores specified exceptions cleanly without verbose `try-except-pass` boilerplate:
```python
import os
from contextlib import suppress

# Removes file if it exists, silently ignores FileNotFoundError if missing
with suppress(FileNotFoundError):
    os.remove("temp_cache.txt")
```

### 5.2 Multiple Context Managers in One `with` Statement
Comma-separated syntax to chain multiple context managers:
```python
with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
    dst.write(src.read())
```

