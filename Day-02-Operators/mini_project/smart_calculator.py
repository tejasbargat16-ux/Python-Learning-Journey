print("=" * 40)
print("       🧮 SMART CALCULATOR")
print("=" * 40)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, **): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

elif operator == "%":
    result = num1 % num2

elif operator == "**":
    result = num1 ** num2

else:
    result = "Invalid operator"

print("\nResult:", result)

print("=" * 40)
print("        Calculation Complete 🚀")
print("=" * 40)
