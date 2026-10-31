def number_stream(start, end):
    for number in range(start, end + 1):
        yield number


def even_stream(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


try:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > end:
        print("Start must be less than or equal to end.")
    else:
        print("\nAll numbers:")
        for number in number_stream(start, end):
            print(number, end=" ")

        print("\n\nEven numbers:")
        for number in even_stream(start, end):
            print(number, end=" ")

        print()

except ValueError:
    print("Please enter valid integers.")
