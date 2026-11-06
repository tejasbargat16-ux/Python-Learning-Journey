class FileReader:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing...")
        if self.file:
            self.file.close()
        return False


with open("demo.txt", "w") as f:
    f.write("Python is fun")

with FileReader("demo.txt") as f:
    print(f.read())
