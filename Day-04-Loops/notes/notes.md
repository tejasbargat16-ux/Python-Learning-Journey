# Day 04: Loops in Python — Study Notes 🔁

## 1. Overview
Loops are control flow structures that repeat a block of code multiple times until a specified condition is met or a sequence has been completely iterated over.

---

## 2. The `for` Loop
Used for iterating over an iterable sequence (e.g., `range`, `list`, `str`, `tuple`).

```python
for item in ["Python", "JavaScript", "Rust"]:
    print(f"Learning {item}")
```

### The `range()` Function
Generates an arithmetic progression sequence on the fly without storing all numbers in memory:

$$\text{range(start, stop[, step])}$$

- `range(5)`: `0, 1, 2, 3, 4` (starts at 0, stops before 5)
- `range(1, 6)`: `1, 2, 3, 4, 5`
- `range(0, 10, 2)`: `0, 2, 4, 6, 8` (increments by 2)
- `range(10, 0, -1)`: `10, 9, 8, ... 1` (reverse order)

```python
for i in range(1, 6):
    print(i, end=" ")
# Output: 1 2 3 4 5
```

---

## 3. The `while` Loop
Repeatedly executes as long as a condition evaluates to `True`.

```python
count = 1
while count <= 5:
    print(f"Iteration: {count}")
    count += 1  # Crucial to avoid infinite loops!
```

---

## 4. Loop Control Statements

### 4.1 `break`
Immediately terminates the current loop and resumes execution at the next statement outside the loop.

```python
for num in range(1, 10):
    if num == 5:
        break
    print(num, end=" ")
# Output: 1 2 3 4
```

### 4.2 `continue`
Skips the rest of the current iteration and jumps directly to the beginning of the next iteration.

```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num, end=" ")
# Output: 1 2 4 5
```

### 4.3 `pass`
A null statement used as a syntactic placeholder when code is required but no action should be performed.

```python
for i in range(5):
    pass  # To be implemented later
```

---

## 5. Loop `else` Clause
Python loops support an optional `else` block:
- The `else` block executes **only if the loop finishes normally** (without hitting a `break` statement).

```python
# Prime number checker pattern
number = 17
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print(f"{number} is composite (divisible by {i})")
        break
else:
    print(f"{number} is prime!")
```

---

## 6. Nested Loops
A loop placed inside the body of another loop. The inner loop executes completely for each individual cycle of the outer loop.

```python
# Multiplication table grid
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i * j:2d}", end=" ")
    print()
```

---

## 7. Common Pitfalls & Tips
- **Infinite Loops**: Always ensure loop termination variables change within a `while` loop.
- **Off-by-One Errors**: `range(1, 10)` stops at 9, never reaches 10.
- **Modifying sequences while iterating**: Never append or delete from a list while iterating over it directly; iterate over a copy `for item in items[:]:` instead.

