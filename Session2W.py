"""
    OOPS in Python :)
    Object Oriented Programming Structure

    1. Object
    2. Class
    3. Functions in Class
    4. Standardization of Objects -> Constructors :)


    OOPS in real world :)
    ---------------------
    anything in the world which exists in reality is Object
    representation of an object is Class


    OOPS in Computer Science :)
    --------------------------
    we need to store lot of data in multi value containers
    BUT, we have some limitations in multi value containers
    We cannot have customizations :( i.e. we got built in functions and we will just use them as such

    flexible container which can store lot of data -> OBJECT
    OBJECT is a STORAGE CONTAINER (BOX)

    Class is a Textual Representation i.e. via code we are describing the structure of Object

    Principle of OOPS
    -----------------
    1. Think of an Object
    2. Create its Class
    3. Create the Real Object i.e. Container in the memory from the class


    * requirements
    ---------------
    * create an app to schedule the cab for user :)
    * notify the available driver with booking details and complete the trip

    extract the terms where we will have lot of data associated with them to solve problem
    User
        name, phone, email, gender, address
    Driver
        name, phone, email, gender, address, driving_experience, licence_number, cab_registration_number
    Booking
        id, date, time, user, driver, from_location, to_location, fare, kms


    1. Think of an Object
    User, Driver and Booking
        1.1 write as much as data associated with objects
            i.e. attributes or state or data members or instance variables :)


"""
#  2. Create its Class
class User:
    pass

# 3. Create the Real Objects (in the RAM i.e. memory)
uRef1 = User()  # Object Construction Statement
uRef2 = User()  # Object Construction Statement
uRef3 = uRef1   # Reference Copy

print("uRef1 is:", uRef1, hex(id(uRef1)))
print("uRef2 is:", uRef2, hex(id(uRef2)))
print("uRef3 is:", uRef3, hex(id(uRef3)))

# __dict__ is a magic variable which works on objects to represent data inside them as dictionary
print()
print("Data inside the object referred by uRef1 is:", uRef1.__dict__)
print("Data inside the object referred by uRef2 is:", uRef2.__dict__)
print("Data inside the object referred by uRef3 is:", uRef3.__dict__)

# Write Data in Object
uRef1.name = "John"
uRef3.phone = "+91 99999 11111"
uRef1.email = "john@exmaple.com"
uRef1.gender = "male"
uRef3.address = "Redwood Shores"

uRef2.name = "Fionna"
uRef2.phone = "+91 87654 11111"
uRef2.email = "fionna@exmaple.com"
uRef2.geder = "female"
uRef2.adrs = "Pristine Magnum"

print()

print("Data inside the object referred by uRef1 is:", uRef1.__dict__)
print("Data inside the object referred by uRef2 is:", uRef2.__dict__)
print("Data inside the object referred by uRef3 is:", uRef3.__dict__)

print()
uRef1.isPrime = True

del uRef2.phone

print("Data inside the object referred by uRef1 is:", uRef1.__dict__)
print("Data inside the object referred by uRef2 is:", uRef2.__dict__)
print("Data inside the object referred by uRef3 is:", uRef3.__dict__)

