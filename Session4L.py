# Python Decorators :)
# @staticmethod and @classmethod

class DB:

    def __init__(self):
       print("DB Connection Established")

    # @staticmethod -> we need not to have any reference of the object as 1st input
    # i.e. self will not be available here
    @staticmethod
    def insert(sql):
        print("Executing ", sql)



db = DB()
db.insert(sql="insert into Customer values(...)")

# for staticmethod we need not to have any objects
# we can directly execute it with class name :)
DB.insert(sql="insert into Customer values(...)")

class Customer:

    def __init__(self, name=None, phone=None, temperature=None):
        self.name = name
        self.phone = phone
        self.temperature = temperature

    # a regular function in class with 1st input as reference to object :) i.e. self
    def show(self):
        print("{} | {} | {}".format(self.name, self.phone, self.temperature))

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.phone, self.temperature)

    # @classmethod -> gives the first input as reference to class rather than reference to object
    # so it is very much similar to static method, i.e. we can execute it with class instead of object
    # added advantage as compared to static method is we have 1st input as reference to class itself
    @classmethod
    def create_customers(cls):
        customers = []
        file = open("customers.csv", "r")
        lines = file.readlines()
        for line in lines:
            customer = line.split(",")
            # below here we are executing constructor and constructing a new object
            customers.append(cls(name=customer[0], phone=customer[1], temperature=customer[2]))

        return customers

c1 = Customer(name="Kia", phone="+91 90909 10101", temperature=98.1)

customers = Customer.create_customers()
for customer in customers:
    print(customer)