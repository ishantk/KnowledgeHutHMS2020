"""
    OOPS
        object : Multi Value Container
        class  : Textual Representation how object would be
                 we are sort of creating our own data type :)

    makemytrip.com | use case

    1. Think of Object :)
    Object:         OneWayFlightBooking
    Attributes:     from_location, to_location, departure_date, travellers, travel_class

"""

# 2. Create its Class
class OneWayFlightBooking:
    # we are not coding anything in class as of now :)
    # my class is empty as of now :)
    pass

# 3. Create Objects in Memory from the Class
def main():

    # OneWayFlightBooking() -> is construction of new Object in RAM
    # flight1 -> is a reference variable which will hold the HashCode of that Object
    flight1 = OneWayFlightBooking()
    flight2 = OneWayFlightBooking()
    flight3 = flight1   # Reference Copy -> flight1 and flight3 shall refer to the same object
    # above, we got 2 objects and 3 reference variables :)

    num = 10
    print(num, type(num), hex(id(num)))

    print(flight1, type(flight1), hex(id(flight1)))
    print(flight2, type(flight2), hex(id(flight2)))
    print(flight3, type(flight3), hex(id(flight3)))

    print("Data in Object")
    print("Data in Object Referred by flight1 is:", flight1.__dict__)
    print("Data in Object Referred by flight2 is:", flight2.__dict__)
    print("Data in Object Referred by flight3 is:", flight3.__dict__)

    # In Python when we create objects we have access to it via reference variable
    # we can dynamically create as much as attributes in the Object
    flight1.from_location = "Delhi"
    flight3.to_location = "Bangalore"
    flight1.departure_date = "25th December, 2020"
    flight3.travellers = 2
    flight1.travel_class = "economy"

    flight2.from_location = "Mumbai"
    flight2.to_location = "Goa"
    flight2.departure_date = "1st January, 2021"
    flight2.travellers = 4
    flight2.travel_class = "premium economy"
    flight2.wheel_chair = True
    flight2.special_meal = "vegetarian"

    # Update the Data In Object
    flight2.special_meal = "non vegetarian"

    del flight2.wheel_chair

    print()
    print("Data in Object After we wrote Attributes:")
    print("Data in Object Referred by flight1 is:", flight1.__dict__)
    print("Data in Object Referred by flight2 is:", flight2.__dict__)
    print("Data in Object Referred by flight3 is:", flight3.__dict__)


if __name__ == '__main__':
    main()