import json

student = {
    "name": "Tejas",
    "age": 19,
    "course": "B.Tech",
    "skills": ["Python", "Java", "Git"]
}

json_data = json.dumps(student, indent=4)

print(json_data)
print(type(json_data))
