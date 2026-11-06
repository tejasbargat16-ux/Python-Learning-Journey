import time
from datetime import datetime


class OperationLogger:
    def __init__(self, name, logfile="logs.txt"):
        self.name = name
        self.logfile = logfile
        self.start = 0.0

    def _log(self, message):
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.logfile, "a") as f:
            f.write(f"[{stamp}] {self.name}: {message}\n")

    def __enter__(self):
        self.start = time.perf_counter()
        self._log("STARTED")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        if exc_type is None:
            self._log(f"SUCCESS ({elapsed:.2f}s)")
        else:
            self._log(f"FAILED: {exc_value}")
        return False  # exception aage jaane do


def main():
    # 1. Success
    with OperationLogger("Copy data"):
        with open("source.txt", "w") as src:
            src.write("Sample data\n")
        with open("source.txt") as s, open("copy.txt", "w") as d:
            d.write(s.read())
    print("Operation 1 done")

    # 2. ZeroDivisionError
    try:
        with OperationLogger("Divide numbers"):
            print(10 / 0)
    except ZeroDivisionError:
        print("Operation 2 failed (ZeroDivisionError)")

    # 3. Missing file
    try:
        with OperationLogger("Read missing file"):
            with open("missing.txt") as f:
                f.read()
    except FileNotFoundError:
        print("Operation 3 failed (FileNotFoundError)")

    print("\n--- logs.txt ---")
    with open("logs.txt") as f:
        print(f.read())


if __name__ == "__main__":
    main()
