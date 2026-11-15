import math
from dataclasses import dataclass, FrozenInstanceError


@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float


def distance(a: Coordinate, b: Coordinate) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


p1 = Coordinate(0, 0)
p2 = Coordinate(3, 4)

print("Distance:", distance(p1, p2))

try:
    p1.x = 10
except FrozenInstanceError:
    print("Cannot modify a frozen Coordinate")

