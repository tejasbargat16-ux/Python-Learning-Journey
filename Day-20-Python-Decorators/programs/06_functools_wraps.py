from functools import wraps


def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)

        return func(*args, **kwargs)

    return wrapper


@my_decorator
def welcome(name):
    """Display a welcome message."""
    print("Welcome", name)


welcome("Tejas")

print("Function name:", welcome.__name__)
print("Documentation:", welcome.__doc__)