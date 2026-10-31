import re

text = "I am learning Python programming."

result = re.search("Python", text)

if result:
    print("Pattern found!")
    print("Matched text:", result.group())
    print("Start position:", result.start())
else:
    print("Pattern not found.")