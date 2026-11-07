# Day 10: Strings in Python — Study Notes 🧵

## 1. Overview
A string (`str`) is an **immutable**, ordered sequence of Unicode characters. Being immutable means once a string object is created in memory, its characters cannot be modified in place.

```python
text = "Python Programming"
# text[0] = 'J'  -> TypeError: 'str' object does not support item assignment
```

---

## 2. String Indexing & Slicing
Strings support zero-based indexing from the left and negative indexing from the right:

$$\text{string[start : stop : step]}$$

```python
s = "Hello Python"
print(s[0])       # 'H'
print(s[-1])      # 'n'
print(s[0:5])     # 'Hello'
print(s[6:])      # 'Python'
print(s[::-1])    # 'nohtyP olleH' (Reverse string idiom)
```

---

## 3. Essential String Methods

| Method | Description | Example | Result |
|---|---|---|---|
| `lower()`, `upper()` | Case transformation | `"Py".upper()` | `"PY"` |
| `strip()`, `lstrip()`, `rstrip()` | Strips leading/trailing whitespace | `" hi ".strip()` | `"hi"` |
| `replace(old, new[, count])` | Substring substitution | `"cat".replace("c", "b")` | `"bat"` |
| `split(sep)` | Splits string into a list of substrings | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `join(iterable)` | Concatenates list of strings using separator | `"-".join(['a', 'b'])` | `"a-b"` |
| `find(sub)` | Returns lowest index of substring (-1 if not found) | `"code".find("d")` | `2` |
| `count(sub)` | Counts non-overlapping occurrences | `"banana".count("an")` | `2` |
| `startswith()`, `endswith()` | Boolean prefix/suffix check | `"test.py".endswith(".py")`| `True` |
| `isalpha()`, `isdigit()`, `isalnum()` | Character class validation | `"12345".isdigit()` | `True` |

---

## 4. String Formatting Approaches

### 4.1 F-Strings (Formatted String Literals - Recommended)
Introduced in Python 3.6+, evaluate expressions directly inside curly braces `{}`:
```python
name = "Tejas"
day = 10
print(f"Welcome {name}! Day {day:02d} completed successfully.")
print(f"Math calculation: 2 * 3 = {2 * 3}")
```

### 4.2 `str.format()` Method
```python
print("Hello, {}! You have {} unread messages.".format("Tejas", 5))
```

### 4.3 `%` Operator (Legacy Printf Style)
```python
print("Value: %.2f" % 3.14159)  # Value: 3.14
```

---

## 5. String Search & Validation
```python
# Palindrome checker
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))  # True
```

---

## 6. Escape Sequences
- `\n`: Line feed / Newline
- `\t`: Horizontal Tab
- `\\`: Backslash
- `\'`, `\"`: Single and Double quotes
- `r"raw\string"`: Raw strings suppress escape sequence processing (essential for file paths and regex).

