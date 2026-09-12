skills = {"Python", "Git", "SQL", "JavaScript"}

skill = input("Enter a skill: ")

if skill in skills:
    print(skill, "is available.")
else:
    print(skill, "is not available.")
