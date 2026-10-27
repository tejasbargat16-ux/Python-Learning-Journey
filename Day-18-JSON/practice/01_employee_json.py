import json

employee = {
    "name": "Tejas",
    "employee_id": 101,
    "salary": 35000
}

json_data = json.dumps(employee, indent=4)

print(json_data)
print("Data type:", type(json_data))
