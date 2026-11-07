# Day 02: Operators in Python — Study Notes ⚡

## 1. Overview
Operators are special symbols that carry out arithmetic or logical computation on operands (variables or values).

---

## 2. Arithmetic Operators
Used to perform standard mathematical calculations.

| Operator | Meaning | Example (`a = 10, b = 3`) | Result |
|:---:|---|---|:---:|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | True Division (always returns float) | `10 / 3` | `3.3333...` |
| `//` | Floor Division (integer quotient) | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation (power) | `10 ** 3` | `1000` |

---

## 3. Assignment Operators
Used to assign and update values in variables.

| Operator | Equivalent Expression | Example |
|:---:|---|---|
| `=` | `x = 5` | Direct assignment |
| `+=` | `x = x + 3` | Add and assign |
| `-=` | `x = x - 3` | Subtract and assign |
| `*=` | `x = x * 3` | Multiply and assign |
| `/=` | `x = x / 3` | Divide and assign |
| `//=` | `x = x // 3` | Floor divide and assign |
| `%=` | `x = x % 3` | Modulus and assign |
| `**=` | `x = x ** 3` | Exponentiate and assign |

---

## 4. Comparison (Relational) Operators
Evaluate expressions and return a boolean (`True` or `False`).

| Operator | Description | Example | Result |
|:---:|---|---|:---:|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

---

## 5. Logical Operators
Used to combine conditional statements.

| Operator | Condition | Example |
|:---:|---|---|
| `and` | Returns `True` if **both** operands are true | `(5 > 2) and (10 > 5)` -> `True` |
| `or` | Returns `True` if **at least one** operand is true | `(5 < 2) or (10 > 5)` -> `True` |
| `not` | Reverses the logical state | `not(5 > 2)` -> `False` |

> [!NOTE]
> Python uses **short-circuit evaluation**:
> - For `and`, if the first operand is false, the second is not evaluated.
> - For `or`, if the first operand is true, the second is not evaluated.

---

## 6. Membership Operators
Used to test whether a value or variable is found in a sequence (`str`, `list`, `tuple`, `set`, `dict`).

- `in`: Returns `True` if the item is present.
- `not in`: Returns `True` if the item is not present.

```python
langs = ["Python", "C++", "Java"]
print("Python" in langs)     # True
print("Ruby" not in langs)   # True
```

---

## 7. Identity Operators
Test if two variables refer to the exact **same memory location** (not just equal values).

- `is`: Returns `True` if both point to the same object (`id(a) == id(b)`).
- `is not`: Returns `True` if both point to different objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (same values)
print(a is b)   # False (different objects in memory)
print(a is c)   # True  (same reference)
```

---

## 8. Operator Precedence (PEMDAS / BODMAS)
From highest to lowest:
1. `()` Parentheses
2. `**` Exponent
3. `+x`, `-x`, `~x` Unary plus, minus, bitwise NOT
4. `*`, `/`, `//`, `%` Multiplication, division, remainder
5. `+`, `-` Addition, subtraction
6. `<<`, `>>` Bitwise shifts
7. `&`, `^`, `|` Bitwise AND, XOR, OR
8. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` Comparisons & Identity
9. `not` Logical NOT
10. `and` Logical AND
11. `or` Logical OR

