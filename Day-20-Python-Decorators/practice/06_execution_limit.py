from functools import wraps


def limit_calls(max_calls):
    def decorator(func):
        count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count

            if count >= max_calls:
                print("Execution limit reached")
                return None

            count += 1

            print(f"Execution {count}/{max_calls}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_calls(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Tejas")
greet("Rahul")
greet("Amit")
greet("Python")
