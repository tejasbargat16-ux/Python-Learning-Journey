from functools import wraps


def logging_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("\nFunction:", func.__name__)
        print("Function started")

        try:
            result = func(*args, **kwargs)
            return result

        finally:
            print("Function completed")

    return wrapper


@logging_decorator
def add(a, b):
    print("Calculating addition...")
    return a + b


result = add(10, 20)

print("Result:", result)