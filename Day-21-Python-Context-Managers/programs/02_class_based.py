class Demo:
    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
        return False


with Demo() as d:
    print("Inside with block")
