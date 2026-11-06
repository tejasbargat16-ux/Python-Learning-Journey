class SafeBlock:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Error caught: {exc_type.__name__}: {exc_value}")
            return True  # exception suppress
        print("No error")
        return False


with SafeBlock():
    print(10 / 0)

print("Program continues")
