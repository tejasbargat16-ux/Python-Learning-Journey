# Day 06: Lists in Python — Study Notes 📋

## 1. Overview
A list is a built-in, mutable, ordered sequence of elements. Lists can contain heterogeneous data types (integers, strings, booleans, or other lists) and allow duplicate values.

```python
numbers = [10, 20, 30, 40, 50]
mixed = [1, "Tejas", 3.14, True, [10, 20]]
```

---

## 2. Indexing and Slicing
Lists use zero-based indexing and support negative indexing from the end.

```python
data = ["A", "B", "C", "D", "E"]
# Positive:  0    1    2    3    4
# Negative: -5   -4   -3   -2   -1

print(data[0])     # 'A'
print(data[-1])    # 'E'
```

### Slicing Syntax: `list[start:stop:step]`
- `start`: Inclusive start index (default 0).
- `stop`: Exclusive stop index.
- `step`: Stride / step size (default 1).

```python
print(data[1:4])    # ['B', 'C', 'D']
print(data[::2])    # ['A', 'C', 'E']
print(data[::-1])   # ['E', 'D', 'C', 'B', 'A'] (reverses the list)
```

---

## 3. Essential List Methods

| Method | Description | Time Complexity |
|---|---|:---:|
| `append(x)` | Adds element `x` to the end of the list | $O(1)$ |
| `insert(i, x)` | Inserts `x` at index `i` | $O(n)$ |
| `extend(iterable)` | Extends list by appending all elements from iterable | $O(k)$ |
| `remove(x)` | Removes the first occurrence of value `x` (raises `ValueError` if missing) | $O(n)$ |
| `pop([i])` | Removes and returns element at index `i` (default last) | $O(1)$ end / $O(n)$ mid |
| `clear()` | Removes all elements from the list | $O(n)$ |
| `index(x)` | Returns the index of the first occurrence of `x` | $O(n)$ |
| `count(x)` | Returns number of times `x` appears in the list | $O(n)$ |
| `sort()` | Sorts list in-place (Timsort algorithm) | $O(n \log n)$ |
| `reverse()` | Reverses elements in-place | $O(n)$ |

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)        # [3, 1, 4, 1, 5, 9]
nums.sort()           # [1, 1, 3, 4, 5, 9]
popped = nums.pop()   # 9
```

---

## 4. List Comprehensions
A concise and idiomatic way to create lists based on existing sequences:

$$\text{[expression \textbf{for} item \textbf{in} iterable \textbf{if} condition]}$$

```python
# Squares of even numbers from 0 to 9
evens_squared = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

---

## 5. Copying Lists: Shallow vs Deep
- Direct assignment (`b = a`) only creates a reference alias, not a new list.
- **Shallow Copy** (`a.copy()` or `a[:]`): New outer list, but nested objects are still referenced.
- **Deep Copy** (`copy.deepcopy(a)`): Recursively copies all nested structures.

