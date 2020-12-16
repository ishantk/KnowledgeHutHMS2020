"""
    Persistence
    1. DataBase -> MySQL


    SQL:
    create table Customer(
        ...
    )

    ORM | Object Relational Mapping

    Reference link on MySQL Dev Portal: https://dev.mysql.com/doc/connector-python/en/

"""

import mysql.connector as db

class DAO:

    def __init__(self):
        self.connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        self.cursor = self.connection.cursor()

    def release(self):
        self.cursor.close()


class Customer:

    def __init__(self, flag):
        if flag:
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
        # SQL Steps:
        # 1. Make Connection to DataBase
        # 2. Write SQL Statement
        # 3. Execute It with APIs

        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("1. Connection Created :)")

        sql = "insert into Customer values (null, '{}', '{}', {}, '{}')".\
            format(self.name, self.phone, self.temperature, self.entry_time_stamp)
        print("2. SQL Statement:", sql)

        # cursor is the API to write in DB :)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print("3. Customer {} Saved in DB :)".format(self.name))
        cursor.close()


    def update_customer_details(self):
        # SQL Steps:
        # 1. Make Connection to DataBase
        # 2. Write SQL Statement
        # 3. Execute It with APIs

        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("1. Connection Created :)")

        sql = "update Customer set NAME = 'Fionna Flynn', PHONE='+91 90909 10101' where CID=2"
        print("2. SQL Statement:", sql)

        # cursor is the API to write in DB :)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print("3. Customer Updated in DB :)")
        cursor.close()

    def delete_customer_details(self):
        # SQL Steps:
        # 1. Make Connection to DataBase
        # 2. Write SQL Statement
        # 3. Execute It with APIs

        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("1. Connection Created :)")

        sql = "delete from Customer where CID = 1"
        print("2. SQL Statement:", sql)

        # cursor is the API to write in DB :)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print("3. Customer Deleted from DB :)")
        cursor.close()

    def fetch_customers(self):

        try:
            connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
            sql = "select * from Customer"
            cursor = connection.cursor()
            cursor.execute(sql)
            # fetch all the rows from the table as tuples
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            cursor.close()
        except Exception as e:
            print("Something Went Wrong:", e)

def main():

    print("WELCOME")
    print("COVID CUSTOMER WALKIN LOGGER")

    # choice = "yes"
    #
    # while choice == "yes":
    #
    #     c_ref = Customer()
    #     c_ref.show()
    #     c_ref.save_customer_details()
    #
    #     choice = input("Would you like to register new customer walk in to the store (yes/no): ")

    c_ref = Customer(flag=False)
    c_ref.fetch_customers()
    # c_ref.update_customer_details()
    # c_ref.delete_customer_details()

if __name__ == '__main__':
    main()