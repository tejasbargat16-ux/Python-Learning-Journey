from functools import wraps


def repeat_three_times(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        for count in range(1, 4):
            print(f"Execution {count}:")
            func(*args, **kwargs)

    return wrapper


@repeat_three_times
def welcome(name):
    print("Welcome", name)


welcome("Tejas")