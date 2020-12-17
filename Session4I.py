"""
    Magic Methods
    represented with __somename()__
"""

import datetime
today = datetime.datetime.today()

print(today)
print(str(today))   # Textual Representation of Contents of Object
print(repr(today))  # Object Representation with Contents

# class Point(object): # by default classes are child of object
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Point: {} | {}".format(self.x, self.y))

    # Override str function to show contents of Object rather than HashCodes
    def __str__(self):
        return "{},{}".format(self.x, self.y)

    # Override repr function to show Object as String rather than HashCodes
    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    # Operator Overloading with Magic Method
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # Similarly, we can have magic method for every single operator :)


p_ref = Point(x=10, y=20)
print("p_ref:", p_ref)
print("str(p_ref):", str(p_ref))
print("repr(p_ref):", repr(p_ref))

p1 = Point(x=11, y=22)
p2 = Point(x=33, y=44)

p3 = p1 + p2 # -> p3 = Point.__add__(p1, p2) | p3 = p1.__add__(p2)
print(repr(p3))