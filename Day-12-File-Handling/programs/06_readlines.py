# pyrefly: ignore [missing-import]
file = open("student.txt", "r")

lines = file.readlines()

print(lines)

file.close()