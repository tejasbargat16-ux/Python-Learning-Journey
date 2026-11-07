# Day 13: Modules & Packages in Python — Study Notes 📦

## 1. Overview
Modular programming breaks complex applications down into smaller, self-contained, and manageable files.
- **Module**: Any Python file (`.py`) containing functions, classes, and variables.
- **Package**: A directory of Python modules containing an `__init__.py` file (optional in Python 3.3+, but standard practice for namespace packages).

---

## 2. Import Variations

```python
# 1. Full module import
import math
print(math.sqrt(25))

# 2. Specific function/class import
from math import pi, factorial
print(factorial(5))

# 3. Aliasing with 'as' (renaming for brevity or conflict avoidance)
import datetime as dt
import random as rnd
print(rnd.randint(1, 100))

# 4. Wildcard import (Caution: Discouraged due to namespace pollution)
# from math import *
```

---

## 3. The `__name__ == '__main__'` Idiom
Every Python module has a special built-in variable `__name__`:
- When executed directly from the terminal (`python my_script.py`), `__name__` is set to `"__main__"`.
- When imported into another file (`import my_script`), `__name__` is set to the module's file name (`"my_script"`).

```python
def add(a, b):
    return a + b

# Code inside this block runs ONLY when the script is run directly,
# NOT when imported by other modules!
if __name__ == "__main__":
    print("Testing add():", add(2, 3))
```

---

## 4. Standard Library Powerhouse Modules

### 4.1 `math` Module
Mathematical functions and constants:
- `math.ceil()`, `math.floor()`, `math.sqrt()`, `math.pow()`
- `math.sin()`, `math.cos()`, `math.log()`, `math.pi`, `math.e`

### 4.2 `random` Module
Pseudorandom number generation:
- `random.randint(a, b)`: Random integer in $[a, b]$ inclusive.
- `random.choice(sequence)`: Random element from a non-empty sequence.
- `random.shuffle(list)`: In-place shuffling of mutable sequence.
- `random.sample(seq, k)`: Unique random selection of $k$ items.

### 4.3 `datetime` Module
Date, time, and calendar calculations:
```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
tomorrow = date.today() + timedelta(days=1)
```

---

## 5. Creating Custom Packages
Directory structure:
```text
my_toolkit/
├── __init__.py          # Marks directory as package
├── math_tools.py        # Sub-module
└── string_tools.py      # Sub-module
```

Importing from the package:
```python
from my_toolkit.math_tools import calculate_average
```

