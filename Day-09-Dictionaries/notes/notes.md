# Day 09: Dictionaries in Python — Study Notes 📖

## 1. Overview
A dictionary (`dict`) is an unordered (insertion-ordered in Python 3.7+), mutable collection of **key-value pairs**.
- Keys must be **unique** and **hashable** (immutable: `str`, `int`, `tuple`).
- Values can be of any data type and can be duplicated.

```python
student = {
    "name": "Tejas",
    "branch": "ECE",
    "year": 3,
    "skills": ["Python", "Git", "Embedded C"]
}
```

---

## 2. Accessing & Updating Values

### 2.1 Square Bracket Lookup vs `.get()`
- `dict[key]`: Returns value; raises `KeyError` if key does not exist.
- `dict.get(key, default)`: Safely returns value, or `default` (`None` if omitted) if key is missing.

```python
print(student["name"])             # "Tejas"
print(student.get("gpa", "N/A"))   # "N/A" (no KeyError!)
```

### 2.2 Adding and Modifying Items
```python
student["gpa"] = 8.8               # Adds new key "gpa"
student["year"] = 4                # Updates existing key "year"
```

---

## 3. Essential Dictionary Methods

| Method | Description |
|---|---|
| `keys()` | Returns a dynamic view of all keys |
| `values()` | Returns a dynamic view of all values |
| `items()` | Returns a view of `(key, value)` tuple pairs |
| `update(other_dict)` | Merges another dictionary or iterable of key-values |
| `pop(key[, default])` | Removes specified key and returns its value |
| `popitem()` | Removes and returns the last inserted `(key, value)` pair ($LIFO$) |
| `setdefault(key, def)`| Returns value of key; if absent, inserts key with `def` |
| `clear()` | Removes all elements from the dictionary |

```python
marks = {"Math": 90, "Physics": 85, "Python": 95}

for subject, score in marks.items():
    print(f"{subject}: {score}")
```

---

## 4. Dictionary Comprehensions
Create transformed dictionaries cleanly and compactly:

$$\text{\{key\_expr: value\_expr \textbf{for} item \textbf{in} iterable \textbf{if} condition\}}$$

```python
numbers = [1, 2, 3, 4, 5]
cubes = {n: n**3 for n in numbers if n % 2 != 0}
# {1: 1, 3: 27, 5: 125}
```

---

## 5. Nested Dictionaries
Dictionaries can contain other dictionaries to model complex hierarchical schemas:

```python
users = {
    "user_101": {"name": "Tejas", "role": "Admin"},
    "user_102": {"name": "Rahul", "role": "Member"}
}

print(users["user_101"]["role"])  # "Admin"
```

---

## 6. Performance Characteristics
- Key lookup, insertion, and deletion operate in $O(1)$ average time complexity using underlying hash table mechanisms.

