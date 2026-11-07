# Day 08: Sets in Python — Study Notes 🔘

## 1. Overview
A set is an unordered, unindexed collection of **unique**, hashable elements. Sets are mutable, but the elements they contain must be immutable.

```python
fruits = {"apple", "banana", "orange", "apple"}
print(fruits)  # {'orange', 'banana', 'apple'} -> duplicates removed automatically
```

> [!NOTE]
> An empty set must be declared using `set()`. `{}` creates an empty dictionary.

---

## 2. Common Set Methods

| Method | Syntax | Description |
|---|---|---|
| `add(x)` | `s.add(val)` | Adds an element to the set |
| `remove(x)` | `s.remove(val)` | Removes an element; raises `KeyError` if absent |
| `discard(x)` | `s.discard(val)` | Removes an element safely without raising error if absent |
| `pop()` | `s.pop()` | Removes and returns an arbitrary element |
| `clear()` | `s.clear()` | Removes all elements from the set |

```python
primes = {2, 3, 5}
primes.add(7)
primes.discard(10)  # Does not crash even though 10 is missing
```

---

## 3. Mathematical Set Operations

| Operation | Operator | Method | Description |
|---|:---:|---|---|
| **Union** | `A \| B` | `A.union(B)` | All elements in A or B |
| **Intersection** | `A & B` | `A.intersection(B)` | Common elements in both A and B |
| **Difference** | `A - B` | `A.difference(B)` | Elements in A but not in B |
| **Symmetric Difference** | `A ^ B` | `A.symmetric_difference(B)` | Elements in A or B, but not both |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a & b)  # {3, 4}
print(a - b)  # {1, 2}
print(a ^ b)  # {1, 2, 5, 6}
```

---

## 4. Set Comparisons & Subsets
- `A.issubset(B)` or `A <= B`: Tests whether every element of A is in B.
- `A.issuperset(B)` or `A >= B`: Tests whether A contains every element of B.
- `A.isdisjoint(B)`: Returns `True` if A and B have no elements in common.

---

## 5. Frozen Sets (`frozenset`)
An immutable version of a Python set. Since frozensets are hashable, they can be used as keys in dictionaries or elements in other sets.

```python
frozen = frozenset([1, 2, 3])
# frozen.add(4) -> AttributeError: 'frozenset' object has no attribute 'add'
```

---

## 6. Real-World Use Cases
- Fast deduplication: `unique_list = list(set(duplicates_list))`
- $O(1)$ average time complexity membership tests (`if item in my_set:`) compared to $O(n)$ in lists.

