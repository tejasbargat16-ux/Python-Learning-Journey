from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    quantity: int
    tags: list[str] = field(default_factory=list)


p1 = Product("Arduino Uno", 5)
p2 = Product("HC-SR04", 10)

p1.tags.append("microcontroller")
p2.tags.append("sensor")
p2.tags.append("ultrasonic")

print(p1)
print(p2)
print("Same tags list?", p1.tags is p2.tags)
