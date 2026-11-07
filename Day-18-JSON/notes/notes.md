# Day 18: JSON Handling in Python — Study Notes 📋

## 1. Overview
**JSON (JavaScript Object Notation)** is a lightweight, language-independent, human-readable data interchange format widely used in web APIs, configuration files, and data storage.

Python provides the built-in `json` module to encode (serialize) and decode (deserialize) JSON data.

---

## 2. Python to JSON Type Mapping

| Python Object | JSON Equivalent |
|---|---|
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string `""` |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

## 3. Four Core Functions of the `json` Module

### Summary Rule of Thumb:
- Functions ending in **`s`** (`dumps`, `loads`) operate on **S**trings in memory.
- Functions **without `s`** (`dump`, `load`) operate on file-like **stream** objects on disk.

```mermaid
graph LR
    A["Python dict / list"] -->|json.dumps()| B["JSON String (str)"]
    B -->|json.loads()| A
    C["Python dict / list"] -->|json.dump()| D["JSON File on Disk (.json)"]
    D -->|json.load()| C
```

---

## 4. Working with JSON Strings: `dumps` and `loads`

### 4.1 Serialization (`json.dumps()`)
Converts Python objects into JSON-formatted strings.

```python
import json

data = {
    "name": "Tejas",
    "skills": ["Python", "Git", "Embedded C"],
    "active": True,
    "cgpa": 8.8
}

json_str = json.dumps(data, indent=4, sort_keys=True)
print(json_str)
```

### 4.2 Deserialization (`json.loads()`)
Parses a JSON string into corresponding Python data structures.

```python
raw_json = '{"course": "Python 100 Days", "day": 18, "completed": true}'
parsed_dict = json.loads(raw_json)

print(parsed_dict["course"])     # "Python 100 Days"
print(type(parsed_dict))         # <class 'dict'>
```

---

## 5. Working with JSON Files: `dump` and `load`

### 5.1 Writing JSON to File (`json.dump()`)
```python
student_records = [
    {"id": 1, "name": "Tejas", "score": 95},
    {"id": 2, "name": "Rahul", "score": 88}
]

with open("students.json", "w") as file:
    json.dump(student_records, file, indent=4)
```

### 5.2 Reading JSON from File (`json.load()`)
```python
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data:
        print(f"Student: {student['name']} - Score: {student['score']}")
```

---

## 6. Common Pitfalls & Best Practices
- **JSON keys must be strings**: While Python dictionaries allow integers or tuples as keys, standard JSON keys are strictly strings. `json.dumps({1: "one"})` converts key `1` to `"1"`.
- **Handling `json.JSONDecodeError`**: Always wrap `json.loads` or `json.load` inside `try-except` blocks when parsing untrusted external inputs or network payloads:
  ```python
  try:
      obj = json.loads(user_input)
  except json.JSONDecodeError as err:
      print(f"Invalid JSON syntax at line {err.lineno}: {err}")
  ```

