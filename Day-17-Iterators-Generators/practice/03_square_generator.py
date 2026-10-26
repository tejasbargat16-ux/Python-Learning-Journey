def square_generator(n):
    for number in range(1, n + 1):
        yield number ** 2


n = int(input("How many squares? "))

for square in square_generator(n):
    print(square)
