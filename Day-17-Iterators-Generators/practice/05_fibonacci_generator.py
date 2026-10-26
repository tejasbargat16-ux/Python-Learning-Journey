def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("How many Fibonacci numbers? "))

for number in fibonacci(n):
    print(number, end=" ")

print()
