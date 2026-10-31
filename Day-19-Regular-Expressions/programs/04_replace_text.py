import re

text = "Python is difficult. Python is powerful."

updated_text = re.sub(r"Python", "Programming", text)

print(updated_text)