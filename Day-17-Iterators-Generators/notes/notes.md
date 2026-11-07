# Day 17: Iterators and Generators in Python — Study Notes ⚙️

## 1. Overview
Iteration is a fundamental pattern in Python. Understanding the difference between **iterables**, **iterators**, and **generators** is key to writing high-performance, memory-efficient Python code.

---

## 2. Iterables vs Iterators

### 2.1 Iterable
Any object capable of returning its members one at a time.
- Implements `__iter__()` which returns an iterator.
- Examples: `list`, `tuple`, `str`, `dict`, `set`, `range`.

### 2.2 Iterator
The stateful helper object that actually produces values one by one during iteration.
- Implements `__iter__()` (returns `self`) and `__next__()`.
- Calling `next(iterator)` returns the next item.
- When no items remain, it raises `StopIteration`.

```python
numbers = [10, 20, 30]  # Iterable

it = iter(numbers)      # Iterator
print(next(it))         # 10
print(next(it))         # 20
print(next(it))         # 30
# print(next(it))       # Raises StopIteration
```

---

## 3. Building a Custom Iterator
To make a custom class iterable, define:
1. `__iter__(self)`: Returns the iterator object (usually `self`).
2. `__next__(self)`: Computes and returns the next value, or raises `StopIteration`.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for count in Countdown(3):
    print(count, end=" ")  # 3 2 1
```

---

## 4. Generators and the `yield` Keyword
A **generator function** is a simpler, more elegant way to create an iterator using the `yield` keyword instead of boilerplate class methods:
- When a generator encounters `yield`, it pauses function execution, saves local state, and yields the value to the caller.
- When `next()` is called again, execution resumes immediately after the `yield` statement.

```python
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(6):
    print(num, end=" ")  # 0 1 1 2 3 5
```

---

## 5. Generator Expressions
A concise, lazy-evaluated syntax similar to list comprehensions, written with parentheses `()`:

$$\text{(expression \textbf{for} item \textbf{in} iterable \textbf{if} condition)}$$

```python
# List comprehension: Generates all 1,000,000 numbers in RAM immediately
squares_list = [x**2 for x in range(1_000_000)]  # Heavy memory usage!

# Generator expression: Generates one number at a time on demand (Lazy Evaluation)
squares_gen = (x**2 for x in range(1_000_000))   # Almost ZERO memory footprint!

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

---

## 6. Summary Comparison Table

| Feature | List Comprehension | Generator Expression |
|---|---|---|
| **Syntax** | `[x for x in data]` | `(x for x in data)` |
| **Evaluation** | Eager (computes all values immediately) | Lazy (computes on-demand as requested) |
| **Memory** | $O(n)$ proportional to sequence size | $O(1)$ constant memory overhead |
| **Reusability** | Can be indexed, sliced, and iterated repeatedly | Can only be consumed once |

