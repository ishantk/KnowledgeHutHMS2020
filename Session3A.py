"""
    OOPS
        object : Multi Value Container
        class  : Textual Representation how object would be
                 we are sort of creating our own data type :)

    makemytrip.com | use case

    1. Think of Object :)
    Object:         OneWayFlightBooking
    Attributes:     from_location, to_location, departure_date, travellers, travel_class

    Standardization of Object
    Whenever we create an Object, let their be attributes by default in all of them :)

"""

# 2. Create its Class
class OneWayFlightBooking:

    # __init__ is know as constructor
    # self is reference variable, which will hold the hash code of the object in action
    # self is always the 1st input and can be any name of your choice :)
    """
    def __init__(self):
        print("Constructor Executed")
        print("self is:", self)

        self.from_location = None
        self.to_location = None
        self.departure_date = None
        self.travellers = None
        self.travel_class = None
    """

    # Re-Defining the constructor shall overwrite the definition and old constructor is gone :(
    def __init__(self, from_location=None, to_location=None,
                 departure_date=None, travellers=None, travel_class=None):
        print("Constructor Executed")
        print("self is:", self)

        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers
        self.travel_class = travel_class
        self.insurance = True
        self.isUpgraded = False

    # function in a class :)
    # here also 1st input is self and can be any name of your choice
    def upgrade_flight(any_name_for_self):
        any_name_for_self.isUpgraded = True
        any_name_for_self.seat = "spacious leg room"
        any_name_for_self.entertainment = True


    def show_flight_booking_details(self):
        print("~~~~~~~~~~~~~~~~~~~~")
        print(self.from_location, self.to_location)
        if self.isUpgraded:
            print(self.seat)
            print(self.entertainment)
        print("~~~~~~~~~~~~~~~~~~~~")

# 3. Create Objects in Memory from the Class
def main():
    # OneWayFlightBooking() -> object construction statement will execute __init__ constructor automatically
    # and will pass flight1 into self :)
    flight1 = OneWayFlightBooking()
    print("flight1 is:", flight1)

    print()

    flight2 = OneWayFlightBooking(from_location="Mumbai", to_location="Goa", travellers=6)
    print("flight2 is:", flight2)

    print()

    # reference copy -> its not object construction
    flight3 = flight1

    flight2.special_meals = "vegetarian"

    flight3.from_location = "Delhi"

    flight2.upgrade_flight()

    print("Data for flight1:", flight1.__dict__)
    print("Data for flight2:", flight2.__dict__)
    print("Data for flight3:", flight3.__dict__)

    flight1.show_flight_booking_details()
    flight2.show_flight_booking_details()

if __name__ == '__main__':
    main()