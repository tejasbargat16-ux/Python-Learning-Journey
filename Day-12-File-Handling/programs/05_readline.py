file = open("student.txt", "r")

line1 = file.readline()
line2 = file.readline()

print("Line 1:", line1)
print("Line 2:", line2)
file.close()