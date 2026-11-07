# Day 21: Python Context Managers and the `with` Statement

## Overview
Context managers automatically handle setup and cleanup of resources such as files, timers and connections, even when errors occur.

## Learning Objectives
- Understand the `with` statement
- Build class-based context managers (`__enter__`, `__exit__`)
- Handle exceptions inside `__exit__`
- Use `contextlib.contextmanager` and `suppress`

## Concepts Covered
- `with` statement and `as`
- `__enter__` / `__exit__`
- Exception suppression via return value
- Generator-based context managers
- Multiple context managers in one `with`

## Folder Structure
- `programs/` — 6 concept demo programs
- `practice/` — 5 practice exercises
- `mini_project/` — Safe File Operation Logger
- `notes/` — Comprehensive study notes

## Programs
| File | Description |
|---|---|
| 01_with_basics.py | File handling with `with` |
| 02_class_based.py | Basic `__enter__`/`__exit__` |
| 03_exception_handling.py | Suppressing exceptions |
| 04_timer_class.py | Timer context manager |
| 05_contextlib_decorator.py | `@contextmanager` |
| 06_multiple_and_suppress.py | Multiple managers, `suppress` |

## Practice Exercises
1. File reader context manager
2. Generator-based timer
3. Temporary directory changer
4. Selective error suppressor
5. Logging context manager

## Mini Project
**Safe File Operation Logger**: logs start, duration, success or failure of operations to `logs.txt`.

## How to Run
```bash
cd Day-21-Python-Context-Managers/programs
python 01_with_basics.py
```

## Skills Gained
Resource management, exception handling, clean code design, use of `contextlib`.

## Author
Tejas — ECE student | Python Learning Journey

