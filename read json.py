import json
with open("students.json", "r") as file:
    data = json.load(file)
print(data) #print all data
print(" ")

for student in data:
    print(student["name"]) #print just name.
print(" ")

for student in data:
    print(student["age"]) #print age
print(" ")

for student in data:
    print(student["city"]) #print city
print(" ")

