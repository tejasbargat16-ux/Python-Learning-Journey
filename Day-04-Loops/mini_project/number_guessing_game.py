import random

print("=" * 40)
print("        NUMBER GUESSING GAME")
print("=" * 40)

secret_number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("\nGuess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again ")

    elif guess > secret_number:
        print("Too high! Try again ")

    else:
        print("\n Correct!")
        print("You guessed it in", attempts, "attempts.")
        break

print("\nThanks for playing! ")
