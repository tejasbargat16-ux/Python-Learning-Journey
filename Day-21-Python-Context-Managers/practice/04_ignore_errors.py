class IgnoreErrors:
    def __init__(self, *exceptions):
        self.exceptions = exceptions  # tuple of exception types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            print(f"Suppressed: {exc_type.__name__} - {exc_value}")
            return True
        return False


with IgnoreErrors(ZeroDivisionError, KeyError):
    print(10 / 0)

print("Next line runs")

try:
    with IgnoreErrors(ZeroDivisionError):
        int("abc")
except ValueError as e:
    print(f"ValueError not suppressed: {e}")
