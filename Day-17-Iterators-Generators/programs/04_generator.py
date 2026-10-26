def count_up(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


for value in count_up(5):
    print(value)
