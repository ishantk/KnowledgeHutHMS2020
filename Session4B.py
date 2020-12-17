import csv

# Save Data in File
"""
customers = [
    ('John', "john@example.com", 25),
    ('Fionna', "fionna@example.com", 22),
    ('Kia', "kia@example.com", 35),
    ('Liam', "liam@example.com", 15),
    ('Sia', "sia@example.com", 45),
]

file = open("customers-18dec-2020.csv", "w", newline='')
writer_ref = csv.writer(file)

# for customer in customers:
#     writer_ref.writerow(customer)

writer_ref.writerows(customers)

file.close()
print("Data Saved")
"""

"""
file = open("customers-18dec-2020.csv", "r", newline='')
reader_ref = csv.reader(file)
for customer in reader_ref:
    print(customer)
"""

"""
students = [
    {"roll": 101, "name": "john", "email": "john@example.com", "age": 20},
    {"roll": 201, "name": "jennie", "email": "jennie@example.com", "age": 22},
    {"roll": 301, "name": "jim", "email": "jim@example.com", "age": 24}
]

file = open("students-17dec-2020.csv", 'w', newline='')
# extract all the keys
keys = list(students[0].keys())
writer_ref = csv.DictWriter(file, fieldnames=keys)
writer_ref.writeheader() # i.e. create header for CSV File
writer_ref.writerows(students)
file.close()

print("Data from Dictionary Saved as CSV File :)")
"""

file = open("students-17dec-2020.csv", 'r', newline='')
reader_ref = csv.DictReader(file)
print(reader_ref.fieldnames)
for row in reader_ref:
    print(type(row))
