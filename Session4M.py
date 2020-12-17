# Generator in Python

def customer_generator():

    file = open("customers.csv", "r")

    lines = file.readlines()

    for line in lines:
        yield line


result = customer_generator()
print(type(result))

# print(next(result))
# print(next(result))
# print(next(result))

while True:
    try:
        print(next(result))
    except StopIteration as error:
        print("We are Done With Results")
        break
