try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Successfully entered:", number)
