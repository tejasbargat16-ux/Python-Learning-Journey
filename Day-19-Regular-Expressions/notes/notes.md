# Day 19: Regular Expressions (Regex) in Python — Study Notes 🔍

## 1. Overview
A **Regular Expression (Regex)** is a sequence of characters that forms a search pattern used for text validation, pattern matching, extraction, and string manipulation.

Python provides the built-in `re` module for regular expressions.

---

## 2. Raw String Notation (`r"..."`)
Always define regex patterns using raw strings prefixed with `r` so backslashes `\` are not treated as Python string escape characters:

```python
import re

pattern = r"\d+"  # Raw string ensures \d is passed directly to the regex engine
```

---

## 3. Core `re` Module Functions

| Function | Description | Return Value |
|---|---|---|
| `re.search(pattern, string)` | Scans string for first location where pattern matches | `Match` object or `None` |
| `re.match(pattern, string)` | Matches pattern only at the **very beginning** of string | `Match` object or `None` |
| `re.fullmatch(pattern, string)` | Matches pattern against the **entire** string | `Match` object or `None` |
| `re.findall(pattern, string)` | Finds **all** non-overlapping occurrences of pattern | List of strings/tuples |
| `re.finditer(pattern, string)` | Finds all occurrences, returning an iterator of Match objects | Iterator of `Match` objects |
| `re.sub(pattern, repl, string)` | Substitutes occurrences of pattern with replacement | New updated string |
| `re.split(pattern, string)` | Splits string at each match of pattern | List of substrings |

---

## 4. Working with Match Objects

```python
text = "Tejas completed 19 days of Python in 2026."
match = re.search(r"(\d+)\s+days", text)

if match:
    print("Full match:", match.group(0))  # "19 days"
    print("Group 1:", match.group(1))     # "19"
    print("Start index:", match.start())
    print("End index:", match.end())
```

---

## 5. Regex Metacharacters & Syntax Cheat Sheet

### 5.1 Anchors & Metacharacters
- `.` : Any character except newline `\n`
- `^` : Start of string / line
- `$` : End of string / line
- `|` : Alternation (OR operator)
- `()` : Capture group

### 5.2 Quantifiers
- `*` : 0 or more occurrences (greedy)
- `+` : 1 or more occurrences (greedy)
- `?` : 0 or 1 occurrence (optional)
- `{n}` : Exactly $n$ times
- `{min, max}` : Between $min$ and $max$ occurrences

### 5.3 Special Character Classes
- `\d` : Any digit `[0-9]` | `\D` : Non-digit
- `\w` : Any alphanumeric word character `[a-zA-Z0-9_]` | `\W` : Non-word
- `\s` : Any whitespace (space, tab, newline) | `\S` : Non-whitespace
- `\b` : Word boundary | `\B` : Non-word boundary

---

## 6. Practical Real-World Patterns

### 6.1 Email Validator
```python
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email = "tejas@example.com"
if re.fullmatch(email_pattern, email):
    print("Valid Email")
```

### 6.2 Extracting Numbers
```python
text = "The items cost $15, $45, and $120."
prices = re.findall(r"\d+", text)  # ['15', '45', '120']
```

### 6.3 Cleaning Extra Whitespace
```python
cleaned = re.sub(r"\s+", " ", "Python    is     awesome!").strip()
# "Python is awesome!"
```

