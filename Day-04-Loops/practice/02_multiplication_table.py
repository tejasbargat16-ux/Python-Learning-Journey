# Take the number from the user and print its table.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
