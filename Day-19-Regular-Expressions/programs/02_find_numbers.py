import re

text = "I completed 19 days and solved 25 problems in 2026."

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)