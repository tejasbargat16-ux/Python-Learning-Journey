from dataclasses import dataclass, field


@dataclass
class Course:
    title: str
    topics: list[str] = field(default_factory=list)


c1 = Course("Python")
c1.topics.append("OOP")
c2 = Course("Java")

print(c1.topics)
print(c2.topics)
