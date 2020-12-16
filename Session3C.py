"""
    Inheritance | OOPS
    Parent Child Relationship | IS-A Relation

    What is Inheritance ?
    Having relationship between 2 classes, where child can access members of Parent IFF it do not have them

    RULE:
    if child has member of its own, it will access it
    else, it will look up in Parent and access it

"""

class Parent:

    def __init__(self):
        print("Parent Object Constructor and self is:", self)
        self.name = "John"
        self.wealth = 10000

    def show(self):
        print("This is show of Parent")


# Inheritance i.e. linking Child and Parent
class Child(Parent):

    def __init__(self):
        print("Child Object Constructor and self is:", self)
        self.name = "Fionna"
        self.wealth = 10000
        self.company_name = "ABC International"

    def show(self):
        print("This is show of Child")



def main():
    p_ref = Parent()
    p_ref.show()

    print()

    print("Dictionary of Parent Object i.e. Data in Object referred by p_ref")
    print(p_ref.__dict__)

    print()

    print("Dictionary of Parent Class i.e. what is inside Parent Class")
    print(Parent.__dict__)

    print()

    print("Dictionary of Child Class i.e. what is inside Child Class")
    print(Child.__dict__)

    print()

    # whenever we create the object, constructor is executed
    # child class has no constructor, but Parent has it so it will use constructor of the Parent
    c_ref = Child()
    print()

    print("Dictionary of Child Object i.e. Data in Object referred by c_ref")
    print(c_ref.__dict__)

    c_ref.show()


if __name__ == '__main__':
    main()