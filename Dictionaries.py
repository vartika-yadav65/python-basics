student = {
    "name": "Rahul",
    "age": 21,
    "course": "CS"
}

print(student["name"])
student["age"] = 22  # birthday update lol

for key, value in student.items():
    print(key, "->", value)