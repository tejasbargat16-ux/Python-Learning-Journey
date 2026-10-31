from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(number):

        if not isinstance(number, (int, float)) or isinstance(number, bool):
            print("Invalid input! Enter a number.")
            return None

        if number <= 0:
            print("Error: Number must be positive.")
            return None

        return func(number)

    return wrapper


@validate_positive
def calculate_square(number):
    return number ** 2


print("Result:", calculate_square(5))

print("Result:", calculate_square(-3))

print("Result:", calculate_square(0))

print("Result:", calculate_square("hello"))