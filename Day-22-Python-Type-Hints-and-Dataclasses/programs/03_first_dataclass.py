from dataclasses import dataclass


@dataclass
class Student:
    name: str
    roll: int
    marks: float = 0.0


s1 = Student("Tejas", 1, 85.5)
s2 = Student("Tejas", 1, 85.5)

print(s1)
print(s1 == s2)
