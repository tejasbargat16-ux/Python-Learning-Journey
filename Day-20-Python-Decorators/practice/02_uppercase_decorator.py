from functools import wraps


def uppercase(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


@uppercase
def greeting():
    return "hello tejas, welcome to python!"


@uppercase
def message(name):
    return f"Welcome {name}"


print(greeting())
print(message("Tejas"))