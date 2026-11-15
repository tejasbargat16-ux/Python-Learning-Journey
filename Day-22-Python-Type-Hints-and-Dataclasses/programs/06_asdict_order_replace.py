from dataclasses import dataclass, asdict, replace


@dataclass(order=True)
class Item:
    price: float
    name: str


a = Item(50.0, "Pen")
b = Item(20.0, "Pencil")

print(a > b)
print(sorted([a, b]))
print(asdict(a))
print(replace(a, price=60.0))
