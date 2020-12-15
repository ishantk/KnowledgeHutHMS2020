# Functions can have inputs to process
# f(x) = x*x + 1

def f(x):
    result = x*x + 1
    print("f: result is:", result)

def exp(base, n):
    result = base ** n
    print("exp: result is:", result)

def add(num1, num2):
    result = num1 + num2
    print("add: result is:", result)

# in case we re-define the add function, we are actually overwriting the definition of the function
# destroying the old function and creating a new add function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print("add: result is:", result)

f(1)
f(2)
f(3)

print()

exp(2, 3)
exp(3, 3)

print()

# add(10, 20) -> now this will be error :(
add(10, 20, 30)
add(-10, 20, -50)




