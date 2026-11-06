with open("sample.txt", "w") as f:
    f.write("Hello Context Manager\n")

print("File closed?", f.closed)

with open("sample.txt", "r") as f:
    print(f.read())
