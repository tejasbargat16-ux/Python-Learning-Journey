from functools import wraps
from datetime import datetime
from time import perf_counter


def monitor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = perf_counter()

        print("\nFunction:", func.__name__)
        print("Started:", datetime.now())

        try:
            result = func(*args, **kwargs)
            return result

        finally:
            end = perf_counter()

            print("Execution time:", round(end - start, 6), "seconds")
            print("Completed:", datetime.now())

    return wrapper


@monitor
def calculate_sum(n):

    total = 0

    for number in range(1, n + 1):
        total += number

    return total


@monitor
def calculate_square(number):
    return number ** 2


print("Sum:", calculate_sum(100000))
print("Square:", calculate_square(12))