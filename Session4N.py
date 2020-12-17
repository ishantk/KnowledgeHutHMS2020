"""
    protected, private, Property
"""

"""
class Point:

    def __init__(self, x, y, z):
        self.x = x      # x is public
        self._y = y     # _y is known as protected in python | and its a warning for user not to access it :)
        self.__z = z    # __z is know as private in python | not accessible

    def show_point(self):
        print("Point is: {} | {} | {}".format(self.x, self._y, self.__z))

def main():
    p1 = Point(x=10, y=20, z=30)
    p1.show_point()

    # print(p1.x)
    # print(p1._y)
    # print(p1.__z)   # not accessible outside the class

    print(p1.__dict__)
    # __z -> converted to _Point__z -> NAME MANGLING
    print(p1._Point__z)

if __name__ == '__main__':
    main()

"""

"""
class Point:

    # if we create variables in class, they belong to class
    # this guy is common variable for all the objects
    total = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.total += 1

    def show(self):
        print("x is:", self.x, "and y is:", self.y)
        print("Total [self.total] is:", self.total)
        print("Total [Point.total] is:", Point.total)


p1 = Point(x=10, y=20)
p2 = Point(x=11, y=22)

print("p1.__dict__:", p1.__dict__)
print("p2.__dict__:", p2.__dict__)

print("Point.__dict__", Point.__dict__)

p1.show()
p2.show()

print("Point total is:", Point.total)
"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # getter | returns the value of attribute
    def get_x(self):
        print("Getting X")
        return self._x

    # setter | setting the value with some validation
    def set_x(self, x):
        print("Setting X")
        if x < 0:
            self._x = 0
        else:
            self._x = x

    # getter | returns the value of attribute
    def get_y(self):
        print("Getting Y")
        return self._y

    # setter | setting the value with some validation
    def set_y(self, y):
        print("Setting Y")
        if y < 0:
            self._y = 0
        else:
            self._y = y

    # creating property object in python
    x = property(get_x, set_x)
    y = property(get_y, set_y)


p1 = Point(-10, 20)
print(p1.__dict__)

print(p1.x)
print(p1.y)


# dataclasses
# https://docs.python.org/3/library/dataclasses.html
