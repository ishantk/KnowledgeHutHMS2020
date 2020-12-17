"""
    XML Module
    Extensible Markup Language

    <students>
        <student>
            <roll>101</roll>
            <name>John</name>
            <email>john@example.com</email>
            <age>20</age>
        </student>
    </students>

"""
# import xml

import xml.etree.ElementTree as xml

"""
students = [
    {"roll": 101, "name": "john", "email": "john@example.com", "age": 20},
    {"roll": 201, "name": "jennie", "email": "jennie@example.com", "age": 22},
    {"roll": 301, "name": "jim", "email": "jim@example.com", "age": 24}
]

root_element = xml.Element("students")

for student in students:
    child = xml.Element("student")
    root_element.append(child)

    roll_element = xml.SubElement(child, "roll")
    roll_element.text = str(student["roll"])

    name_element = xml.SubElement(child, "name")
    name_element.text = student["name"]

    email_element = xml.SubElement(child, "email")
    email_element.text = student["email"]

    age_element = xml.SubElement(child, "age")
    age_element.text = str(student["age"])

tree = xml.ElementTree(root_element)

# file = open("students.xml", "wb")
# tree.write(file)

with open("students.xml", "wb") as file:
    tree.write(file)    # write uses bytes to write in file

print("Data Saved in XML File", file.name)
"""

# XML Parsing
tree = xml.ElementTree(file="students.xml")
root_element = tree.getroot()
print(root_element)

students = []
children = root_element.getchildren()
for child in children:
    student = {}
    pairs = child.getchildren()

    for pair in pairs:
        if pair.tag == 'roll' or pair.tag == 'age':
            student[pair.tag] = int(pair.text)
        else:
            student[pair.tag] = pair.text

    students.append(student)

print(students)


# DOM APIs  | Document Object Model [Tree Data Structure]
# SAX APIs  | Simple API for XML    [Read File as Stream of Events]