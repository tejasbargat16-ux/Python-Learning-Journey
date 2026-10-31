def multiplier(number):

    def calculate(value):
        return value * number

    return calculate


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))