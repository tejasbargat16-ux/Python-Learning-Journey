from datetime import datetime


class LogContext:
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def _write(self, message):
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"[{stamp}] {message}\n")

    def __enter__(self):
        self._write("START")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._write(f"ERROR: {exc_value}")
        self._write("END")
        return False


with LogContext():
    print("Working...")

try:
    with LogContext():
        raise ValueError("Something broke")
except ValueError:
    print("Error handled outside")

print(open("log.txt").read())
