"""
    Decorator
        which takes some function as input and adds some more functionality and returns it
"""



# Function Taking Input as Reference to the Other Function
def upgrade_to_meal(func):

    # Nested Function: Creating Function in a Function -> Local Function
    def upgrade():
        func()
        print("Meal Upgrade: Add Fries and Coke for Burger")

    # Functions Returning Functions :)
    return upgrade


@upgrade_to_meal # decorator -> syntatic sugar
def order_burger():
    print("Order Veggie Burger")

@upgrade_to_meal
def order_wrap():
    print("Order Wrap")

# Generally we decorate the function by reassigning a returned function hashcode

# Decoration :)
# order_burger = upgrade_to_meal(order_burger)


def main():
    # order_burger()
    
    # meal = upgrade_to_meal(order_burger)
    # meal()
    
    order_burger()

    print()

    order_wrap()

if __name__ == '__main__':
    main()