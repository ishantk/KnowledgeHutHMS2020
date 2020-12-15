# Functions return data
# if you dont, every function by defaut returns and returns nothing

"""
def add(num1, num2):
    sum = num1 + num2
    print("sum is:", sum)
    # return # we put return or we do not put return last statement means return


print("This is my first statement to be executed")

add(10, 20)
add(10.5, 20.6)
add("John", "Watson")
# add(10, "Watson") # error
# add(True, False)

print("This is my last statement to be executed")

"""

def add(num1, num2):
    sum = num1 + num2
    return sum


result = add(10, 20)
print("result is:", result)
print("result is:", add(-10, 50))

