# Day 07: Tuples in Python — Study Notes 📦

## 1. Overview
A tuple is an ordered, **immutable** sequence of Python objects. Once created, elements inside a tuple cannot be modified, appended, or removed.

```python
point = (10, 20)
student = ("Tejas", 21, "ECE", 8.8)
```

> [!NOTE]
> Single-element tuples require a trailing comma, otherwise Python treats parentheses as a mathematical expression:
> ```python
> not_a_tuple = (42)    # type is int
> is_a_tuple = (42,)    # type is tuple
> ```

---

## 2. Why Use Tuples Instead of Lists?
1. **Immutability (Data Safety)**: Guarantees that constant or configuration data will not be accidentally mutated.
2. **Performance**: Tuples use less memory and have faster creation/iteration overhead than lists.
3. **Dictionary Keys**: Because tuples are hashable (provided their contents are hashable), they can serve as dictionary keys and set members, whereas lists cannot.

---

## 3. Tuple Indexing & Slicing
Tuples support standard zero-based positive indexing, negative indexing, and slicing identical to lists:

```python
coords = (10, 20, 30, 40, 50)
print(coords[0])      # 10
print(coords[-1])     # 50
print(coords[1:4])    # (20, 30, 40)
```

---

## 4. Tuple Packing and Unpacking

### 4.1 Packing
Assigning multiple comma-separated values into a single tuple without explicit parentheses:
```python
user_data = "Tejas", 20, "Student"  # Automatically packed into a tuple
```

### 4.2 Unpacking
Extracting tuple elements into individual variables:
```python
name, age, role = user_data
print(name)  # "Tejas"
print(age)   # 20
```

### 4.3 Extended Unpacking (`*` operator)
```python
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4, 5]
print(last)    # 6
```

---

## 5. Built-in Tuple Methods
Since tuples are immutable, they only offer two read-only methods:
- `count(x)`: Returns the number of occurrences of `x`.
- `index(x)`: Returns the index of the first occurrence of `x` (raises `ValueError` if not found).

```python
grades = ('A', 'B', 'A', 'A', 'C')
print(grades.count('A'))  # 3
print(grades.index('B'))  # 1
```

---

## 6. Immutability with Mutable Elements
A tuple's references cannot change, but mutable objects inside a tuple can still be mutated:

```python
t = (1, [10, 20], 3)
t[1].append(30)  # Allowed! Mutates the underlying list inside the tuple
print(t)         # (1, [10, 20, 30], 3)
```

