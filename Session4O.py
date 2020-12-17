"""
    JSON: is JavaScript Object Notation
    it is a dictionary as String :)
"""

import json

student = {
    'roll': 101,
    'name': "John",
    'address': {
        'adrsline': 2144,
        'city': "Bangalore",
        'state': "Karnataka"
     },
     'subjects': ["maths", "physics", "chemistry"]
}

print(student)
print(type(student))

print()

json_data = json.dumps(student)

print(json_data)
print(type(json_data))

print()
python_dictionary = json.loads(json_data)

print(python_dictionary)
print(type(python_dictionary))
