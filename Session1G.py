# Controller
# Conditional Flows :)

"""
    WELCOME
    Get 50% OFF up to ₹100.
    On orders above ₹149

    HSBCFIRST
    Get flat 30% OFF using HSBC Credit Card.
    Valid on orders above ₹500.

"""

message = """

    Welcome to ZOMATO
    Order Now :)
    
    -------
    WELCOME
    -------
    Get 50% OFF up to ₹100.
    On orders above ₹149

    ---------
    HSBCFIRST
    ---------
    Get flat 30% OFF using HSBC Credit Card.
    Valid on orders above ₹500.
"""

print(message)

amount = float(input("Enter Amount: "))
promo_code = input("Enter Promo Code: ")

print("amount is:", amount)
print("promo_code is:", promo_code)

# Regular if/else
"""
if amount > 149:
    print("Promo Code can be Applied")
else:
    print("Promo Code Not Applicable")
"""
# Ladder if/else
if amount > 149:

    # Nested if/else
    if promo_code == "WELCOME":

        discount = 0.50 * amount

        if discount > 100:
            discount = 100

        amount -= discount
        print("WELCOME PROMO CODE APPLIED")
        print("Discount: $", discount)
        print("Please Pay: $", amount)

    elif (promo_code == "HSBCFIRST") and (amount > 500):    # ok
    # elif (promo_code is "HSBCFIRST") and (amount > 500):  # fails

        discount = 0.30 * amount
        amount -= discount

        print("HSBCFIRST PROMO CODE APPLIED")
        print("Discount: $", discount)
        print("Please Pay: $", amount)

    else:
        print("Promo Code", promo_code, "not valid :(")
        print("Please Pay: $", amount)


# assignment: if user enters a wrong promo code, suggest the right one