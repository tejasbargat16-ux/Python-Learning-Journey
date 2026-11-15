def add(a: int, b: int) -> int:
    return a + b


def greet(name: str, city: str | None = None) -> str:
    if city:
        return f"Hello {name} from {city}"
    return f"Hello {name}"


marks: list[int] = [80, 90, 75]
info: dict[str, int] = {"year": 2}

print(add(2, 3))
print(greet("Tejas"))
print(greet("Tejas", "Wardha"))
print(add("Py", "thon"))  # hints enforce nahi hote
