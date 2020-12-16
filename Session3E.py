"""
    Use Case:
    Covid Scenario: if someone visits a store,
    store maintains the data of customer coming to it

    Customer
        name, phone, temperature, entry_time_stamp


    Persistence:
    Save the state of an Object
    Objects will hold data in the memory i.e. RAM which is temporary
    Whenever main finishes app is finished and hence data is lost
    1. Files
    2. DataBases | SQL, NoSQL, Graph....
        Local
        Cloud
"""


class Customer:

    def __init__(self):
        print("Register a New Customer Walkin")
        self.name = input("Enter Name: ")
        self.phone = input("Enter Phone: ")
        self.temperature = float(input("Enter Temperature: "))
        self.entry_time_stamp = input("Enter Time Stamp: ")

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Customer Details: {} | {} | {} | {}"
              .format(self.name, self.phone, self.temperature, self.entry_time_stamp))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

    def save_customer_details(self):
        # w mode -> overwrites the contents in the file
        # file = open("customers.csv", "w")
        file = open("customers.csv", "a")
        data = "{},{},{},{}\n".format(self.name, self.phone, self.temperature, self.entry_time_stamp)
        file.write(data)
        file.close() # release the memory resources
        print("Customer {} saved in file".format(self.name))

def main():

    print("WELCOME")
    print("COVID CUSTOMER WALKIN LOGGER")

    choice = "yes"

    while choice == "yes":

        c_ref = Customer()
        c_ref.show()
        c_ref.save_customer_details()

        choice = input("Would you like to register new customer walk in to the store (yes/no): ")


if __name__ == '__main__':
    main()