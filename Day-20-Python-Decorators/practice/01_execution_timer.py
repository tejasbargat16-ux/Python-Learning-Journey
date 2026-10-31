import time
from functools import wraps


def execution_timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        execution_time = end - start

        print("Execution time:", round(execution_time, 6), "seconds")

        return result

    return wrapper


@execution_timer
def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total


result = calculate_sum(100000)

print("Sum:", result)