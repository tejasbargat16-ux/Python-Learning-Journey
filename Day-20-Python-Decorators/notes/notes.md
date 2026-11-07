# Day 20: Python Decorators — Study Notes 🎭

## 1. Foundations of Decorators

Before understanding decorators, you must understand three core Python language behaviors:
1. **Functions are First-Class Objects**: Functions can be passed as arguments to other functions, assigned to variables, and returned from functions.
2. **Nested (Inner) Functions**: Functions can be defined inside other functions.
3. **Closures**: An inner function that remembers and retains access to variables in its enclosing scope even after the outer function has finished executing.

```python
# Closure Example
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' is retained in closure
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

---

## 2. What is a Decorator?
A **decorator** is a callable (typically a function) that takes another function as an argument, extends or modifies its behavior without altering its source code, and returns the modified function.

### The `@` Syntactic Sugar
Writing:
```python
@my_decorator
def greet():
    print("Hello")
```
Is mathematically and functionally identical to:
```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

---

## 3. Basic Decorator Pattern
Using `*args` and `**kwargs` allows the wrapper to accept any function signature:

```python
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Completed: {func.__name__}")
        return result
    return wrapper

@my_logger
def add(a, b):
    return a + b

print(add(10, 20))
```

---

## 4. Preserving Function Metadata with `functools.wraps`
When a function is wrapped, its original `__name__`, `__doc__`, and signature are obscured by the wrapper function. `functools.wraps` copies the original function's metadata back to the wrapper:

```python
from functools import wraps

def timing_decorator(func):
    @wraps(func)  # Preserves func.__name__ and docstrings
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timing_decorator
def calculate_cube(n):
    """Calculates the cube of a number."""
    return n ** 3

print(calculate_cube.__name__)  # 'calculate_cube' (without @wraps, it would be 'wrapper')
print(calculate_cube.__doc__)   # 'Calculates the cube of a number.'
```

---

## 5. Decorators with Arguments (Decorator Factories)
When a decorator itself needs configuration parameters (e.g., `@limit_calls(3)` or `@repeat(times=5)`), an additional outer function layer is required:

```python
from functools import wraps

def limit_calls(max_calls):
    def decorator(func):
        count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_calls:
                print(f"Execution limit of {max_calls} reached for {func.__name__}!")
                return None
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(2)
def ping(server):
    print(f"Pinging {server}...")

ping("192.168.1.1")  # Call 1
ping("192.168.1.1")  # Call 2
ping("192.168.1.1")  # Limit reached!
```

---

## 6. Popular Real-World Decorator Applications
- **Execution Timing / Profiling**: Measuring performance benchmarks using `time.perf_counter()`.
- **Authentication & Authorization**: Checking permissions before executing route handlers in Flask/Django.
- **Input Validation & Sanitization**: Verifying argument types and constraints before processing.
- **Caching & Memoization**: `@functools.lru_cache(maxsize=128)` for storing expensive recursive calculations.
- **Rate Limiting & Retries**: Automatic exponential backoff for network APIs.

