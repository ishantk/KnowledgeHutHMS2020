"""
    Object Serialization and DeSerialization
    pickle
"""
# import pickle as p
import pickle

# Serialization and DeSerialization which is used by Python APIs internally
# import marshal # -> assignment (explore it)

# Dictionary Serialization
# file = open("student_101.txt", "wb")
# student = {"roll": 101, "name": "john", "email": "john@example.com", "age": 20}
# pickle.dump(student, file)
# file.close()
# print("Dictionary Serialized")

# Dictionary DeSerialization
# file = open("student_101.txt", "rb")
# student = pickle.load(file)
# print(student, type(student))
# file.close()

class Student:

    def __init__(self, roll=None, name=None, phone=None, email=None, address=None):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def show(self):
        print("{} | {} | {}".format(self.roll, self.name, self.phone))
        print("{} | {}".format(self.email, self.address))


# Object Serialization
# s_ref = Student(roll=1101, name="Fionna Flynn", phone="+91 99999 11111",
#                 email="fionna@example.com", address="Redwood Shores")
# s_ref.show()
#
# file = open("student-1101.txt", "wb")
# pickle.dump(s_ref, file)
# file.close()
# print("Student Saved :)")

# Object De-Serialization
file = open("student-1101.txt", "rb")
result = pickle.load(file)
print(result)
result.show()