from dataclasses import dataclass, field, FrozenInstanceError


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area = self.width * self.height


@dataclass(frozen=True)
class Point:
    x: int
    y: int


print(Rectangle(4, 5))

try:
    Rectangle(-1, 5)
except ValueError as e:
    print("Error:", e)

p = Point(1, 2)
print(p)

try:
    p.x = 10
except FrozenInstanceError:
    print("Frozen: cannot modify")
