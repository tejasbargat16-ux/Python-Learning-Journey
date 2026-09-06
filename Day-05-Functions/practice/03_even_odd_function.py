def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))

result = check_even_odd(number)

print(number, "is", result)
