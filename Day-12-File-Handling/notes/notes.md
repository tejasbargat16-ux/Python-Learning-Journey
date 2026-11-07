# Day 12: File Handling in Python — Study Notes 📁

## 1. Overview
File handling enables Python programs to read from and write data to persistent storage on disk. Python provides built-in functions such as `open()` without requiring external libraries.

---

## 2. File Access Modes
The `open(filename, mode)` function accepts mode flags:

| Mode | Name | Description | Pointer Position | Creates File? | Truncates (Clears)? |
|:---:|:---:|---|:---:|:---:|:---:|
| `'r'` | Read | Opens existing file for reading | Start | ❌ (Error if missing) | ❌ |
| `'w'` | Write | Opens for writing; creates new or overwrites | Start | ✅ | ✅ |
| `'a'` | Append | Opens for writing; appends data at end | End | ✅ | ❌ |
| `'r+'` | Read/Write | Reads and writes without truncating | Start | ❌ | ❌ |
| `'w+'` | Write/Read | Writes and reads; clears existing content | Start | ✅ | ✅ |
| `'a+'` | Append/Read| Reads and appends | End | ✅ | ❌ |
| `'b'` | Binary | Binary mode (e.g. `'rb'`, `'wb'` for images/PDFs)| - | - | - |

---

## 3. Reading from Files

```python
# 1. read([size]): Reads entire content or up to 'size' characters
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 2. readline(): Reads a single line (including newline \n)
with open("sample.txt", "r") as file:
    first_line = file.readline()

# 3. readlines(): Reads all lines into a list of strings
with open("sample.txt", "r") as file:
    lines = file.readlines()

# 4. Iterating directly over the file object (Memory Efficient for large files)
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        print(f"Line {line_num}: {line.strip()}")
```

---

## 4. Writing to Files

```python
# Overwriting with 'w'
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.writelines(["Line 1\n", "Line 2\n"])

# Appending with 'a'
with open("output.txt", "a") as file:
    file.write("Appended log entry\n")
```

---

## 5. The `with` Statement (Context Manager)
Always use the `with` statement when opening files:
- It automatically invokes the file's `.close()` method as soon as the block exits.
- Ensures files close even if an unhandled exception or crash occurs inside the block.

```python
# Preferred & Pythonic:
with open("data.txt", "r") as f:
    data = f.read()
# f.closed is automatically True here
```

---

## 6. Safe File Operations (Error Handling)
```python
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The requested file could not be found.")
except PermissionError:
    print("Error: You do not have permissions to read this file.")
```

