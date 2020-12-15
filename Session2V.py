# Dictionary

employee = {
    "eid": 101,
    "name": "John",
    "designation": "Lead Engineer",
    "salary": 50000,
    "technology": "Python"
}

print(employee)
print(type(employee))
print(len(employee))
print("Max:", max(employee))
print("Min:", min(employee))

# Update data in Dictionary
employee["salary"] = 70000
print(employee)

# Add extra key/value pairs
employee["email"] = "john@example.com"
print(employee)

# remove key value pair
del employee["technology"]
print(employee)

print("KEYS:")
keys = list(employee.keys())
for key in keys:
    print(key)

print()

print("VALUES:")
values = list(employee.values())
for value in values:
    print(value)

# employee.clear()
# print(employee)

print()

print("ENHANCED FOR LOOP")

for key in employee:
    print(key, "\t", employee[key])

# for value in employee.values():
#     print(value)

print()
print("ITEM ITERATE")
# items = list(employee.items())
for item in employee.items():
    print(item)
    print(item[0], item[1])
    print()

for key, value in employee.items():
    print(key, value)