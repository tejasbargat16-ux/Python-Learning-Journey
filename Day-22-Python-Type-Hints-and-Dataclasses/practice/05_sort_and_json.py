import json
from dataclasses import dataclass, asdict


@dataclass
class Student:
    name: str
    roll: int
    marks: float


students = [
    Student("Amit", 1, 72.5),
    Student("Tejas", 2, 88.0),
    Student("Neha", 3, 95.5),
    Student("Ravi", 4, 64.0),
]

ranked = sorted(students, key=lambda s: s.marks, reverse=True)

for s in ranked:
    print(s)

print(json.dumps([asdict(s) for s in ranked], indent=2))
