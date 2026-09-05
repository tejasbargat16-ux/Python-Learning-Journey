# Do the zero sum of numbers from 1 to 5.

n = int(input("Enter a number: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum:", total)
