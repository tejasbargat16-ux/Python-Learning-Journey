import time
from contextlib import contextmanager


@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] took {elapsed:.4f} seconds")


with timer("Loop"):
    total = 0
    for i in range(1_000_000):
        total += i
    print("Loop done")
