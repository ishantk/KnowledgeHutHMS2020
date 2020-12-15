"""
    Sequences in Python
    Multi Value Containers in Python

    1. tuple
    2. list
    3. set
    4. dictionary
    5. string

    Operations on Sequences (May or May not work with all)
    1. Concatenation
    2. Repetition
    3. Membership Testing
    4. Indexing
    5. Slicing
"""

# students = ["john", "jennie", "jim", "jack", "joe"]
students = ("john", "jennie", "jim", "jack", "joe")
# students = {"john", "jennie", "jim", "jack", "joe"}
print(students)
print(type(students))

print()

#  1. Concatenation
# more_students = students + ["kia", "dave", "harry"]
more_students = students + ("kia", "dave", "harry")
print("students:", students)
print("more_students:", more_students)

# 2. Repetition
repeated_students = students * 3
print("repeated_students:", repeated_students)

print()

# 3. Membership Testing
print("john" in students)
print("lee" not in students)

# 4. Indexing
print(students[0])
print(students[len(students)-1])
# print(students[100]) # error

# 5. Slicing
print(students[0:3]) # from 0 less than 3 i.e. till 2

print()

# Loops on Sequences
for i in range(len(students)):
    print(students[i])

print()

for name in students:
    print(name)