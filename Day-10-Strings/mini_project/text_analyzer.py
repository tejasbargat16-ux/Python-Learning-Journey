text = input("Enter text: ")

words = text.split()

vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("\n===== TEXT ANALYZER =====")

print("Characters:", len(text))
print("Words:", len(words))
print("Python count:", text.lower().count("python"))
print("Vowels:", vowels)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed text:", text[::-1])
