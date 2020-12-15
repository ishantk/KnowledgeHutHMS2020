"""
    Default Arguments
"""

# def add(num1=10, num2, num3):  # error
# def add(num1, num2=1, num3):   # error
# def add(num1=1, num2=1, num3): # error


# def add(num1, num2=-1, num3=5): # OK
def add(num1=0, num2=-1, num3=5): # OK
    sum = num1 + num2 + num3
    print("Sum of {} {} and {} is {}".format(num1, num2, num3, sum))


add(10, 20, 30)
add(10, 20)
add(10)
add()

add(num1=10, num3=20)

# we can execute the function by passing input name with value :)
add(num1=10, num3=19, num2=100)

