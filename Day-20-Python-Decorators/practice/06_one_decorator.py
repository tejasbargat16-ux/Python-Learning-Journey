import time
from functools import wraps


def monitor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        print("Starting:", func.__name__)

        try:
            result = func(*args, **kwargs)
            return result

        finally:
            end = time.perf_counter()

            print("Completed:", func.__name__)
            print("Time:", round(end - start, 6), "seconds")

    return wrapper


@monitor
def multiply(a, b):
    return a * b


print("Result:", multiply(20, 30))