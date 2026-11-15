# Day 22: Python Type Hints and Dataclasses

## Overview
Type hints make code self-documenting and tool-friendly. Dataclasses remove boilerplate from data-holding classes by auto-generating `__init__`, `__repr__` and `__eq__`.

## Learning Objectives
- Write type hints for variables, parameters and return values
- Create classes using `@dataclass`
- Use `field`, `default_factory`, `__post_init__`, `frozen`, `order`
- Convert dataclasses with `asdict` and copy with `replace`

## Concepts Covered
- Type annotations (`int`, `list[str]`, `X | None`)
- Hints are not enforced at runtime
- `@dataclass` and auto-generated methods
- Mutable defaults with `default_factory`
- Validation with `__post_init__`
- Immutable and sortable dataclasses

## Folder Structure
- `programs/` — 6 concept demos
- `practice/` — 5 exercises
- `mini_project/` — Student Record Manager

## Programs
| File | Description |
|---|---|
| 01_type_hints.py | Type hint basics |
| 02_without_dataclass.py | Manual boilerplate class |
| 03_first_dataclass.py | First `@dataclass` |
| 04_default_factory.py | Safe mutable defaults |
| 05_post_init_frozen.py | Validation and immutability |
| 06_asdict_order_replace.py | Sorting, dict conversion, copying |

## Practice Exercises
1. Book dataclass
2. Employee with validation
3. Product with tags
4. Frozen coordinates with distance
5. Sort students and export JSON

## Mini Project
**Student Record Manager**: dataclass-based records saved to and loaded from JSON with a menu interface.

## How to Run
```bash
cd Day-22-Python-Type-Hints-and-Dataclasses/programs
python 03_first_dataclass.py
```

## Skills Gained
Type annotations, clean data modeling, validation, JSON serialization of objects.

## Author
Tejas — ECE student | Python Learning Journey
