word = input("Enter a word: ")

characters = {}

for char in word:

    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

print("\nCharacter Frequency:")

for char, count in characters.items():
    print(char, ":", count)
