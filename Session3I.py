"""
    Modules in Python
    Any Python Program us known as MODULE :)
    i.e. .py file is a MODULE
"""

print("1. This is Session3I.py")
print("1. Session3I.py name is:", __name__)

name = "John Watson"


def add(num1, num2):
    sum = num1 + num2
    print("Sum is:", sum)


class Order:
    def __init__(self, oid=None, amount=None, customer_email=None):
        self.oid = oid
        self.amount = amount
        self.customer_email = customer_email

    def show(self):
        print("{} | {} | {}".format(self.oid, self.amount, self.customer_email))


def main():
    print("2. This is Session3I.py main")
    print("2. This is Session3I.py main | name is:", __name__)

    add(10, 20)
    o_ref = Order(101, 5000, "john@example.com")
    o_ref.show()


if __name__ == '__main__':
    main()