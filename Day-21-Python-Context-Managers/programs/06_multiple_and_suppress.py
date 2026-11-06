import os
from contextlib import suppress

with open("a.txt", "w") as f1, open("b.txt", "w") as f2:
    f1.write("A")
    f2.write("B")

with suppress(FileNotFoundError):
    os.remove("missing.txt")

print("Done")
