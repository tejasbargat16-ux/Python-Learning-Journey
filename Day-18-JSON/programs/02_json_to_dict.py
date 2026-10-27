import json

json_data = '''
{
    "name": "Tejas",
    "age": 19,
    "language": "Python"
}
'''

student = json.loads(json_data)

print(student)
print("Name:", student["name"])
print("Language:", student["language"])
print(type(student))
