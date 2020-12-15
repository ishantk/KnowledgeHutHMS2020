"""

    Functions in Python
    Piece of logic has to be used again and again
    Use Cases:
    1. For every product we wish to provide some discounts
    2. Cart Value
    3. CheckOut
    4. Invoice billing

    Functions are small set of code snippets as a block with a name given so as to modulaize the program

"""

# use keyword -> def
# give any possible identifier as a name to function -> brackets () at the end of function
# write the definition i.e. what function will do with tab spaces after :

# creating add function
def add():
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number3: "))

    result = number1 + number2

    print("Result is:", result)


# execution of add function
add()
add()