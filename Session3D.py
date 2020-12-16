"""
    Why Inheritance ?
    Code Re Usability :)

    Reference : https://www.makemytrip.com/
    FlightBooking
"""

class OneWayFlightBooking:

    def __init__(self, from_location=None, to_location=None,
                 departure_date=None, travellers=None, travel_class=None):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers
        self.travel_class = travel_class


    def show_flight_booking_details(self):
        print("~~~~~~~~~~~~~~~~~~~~")
        print(self.from_location, self.to_location)
        print(self.departure_date)
        print(self.travellers)
        print(self.travel_class)
        print("~~~~~~~~~~~~~~~~~~~~")


class TwoWayFlightBooking(OneWayFlightBooking):

    def __init__(self, from_location=None, to_location=None,
                 departure_date=None, travellers=None, travel_class=None, return_date=None):
        OneWayFlightBooking.__init__(self, from_location, to_location,
                                     departure_date, travellers, travel_class)

        self.return_date = return_date

    def show_flight_booking_details(self):
        print("~~~~~~~~~~~~~~~~~~~~")
        OneWayFlightBooking.show_flight_booking_details(self)
        print(self.return_date)
        print("~~~~~~~~~~~~~~~~~~~~")


class MultipleFlightBooking(TwoWayFlightBooking):
    pass


def main():
    one_way = OneWayFlightBooking(from_location="Delhi",
                                  to_location="Bangalore", departure_date="25th December 2020",
                                  travellers=4, travel_class="economy")
    one_way.show_flight_booking_details()

    print()

    two_way = TwoWayFlightBooking(from_location="Delhi",
                                  to_location="Bangalore", departure_date="25th December 2020",
                                  return_date="1st January, 2020",
                                  travellers=4, travel_class="economy")
    two_way.show_flight_booking_details()


if __name__ == '__main__':
    main()


"""
    Types of Inheritance
"""

# Single Level Inheritance | 1 Parent 1 Child
class CA:
    pass

class CB(CA):
    pass

# Multi Level   | Parent -> Child -> GrandChild
class CC(CB):
    pass

# Multiple  | 1 Child, Multiple Parents
class CD:
    pass

class CE(CA, CD):
    pass

# Hierarchy | 1 Parent Multiple Children
class CF:
    pass

class CG(CF):
    pass

class CH(CF):
    pass