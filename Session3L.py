# Exception Handling
# Errors at Run Time -> Python is Interpreted and hence error means a Run Time Error

print("Program Started")

num1 = 0
num2 = 0

try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
except ValueError as ref:
    print("Invalid Number Entry")
    print(ref)

result = 0

try:
    result = num1//num2
except ZeroDivisionError as ref:
    print("Something went Wrong")
    print(ref)

print("Result is:", result)

print("Program Finished")