def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)