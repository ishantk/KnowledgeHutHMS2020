# Conversion
numbers1 = (10, 20, 30, 40, 50)
print(numbers1, type(numbers1), id(numbers1))

print()

numbers2 = list(numbers1)
print(numbers2, type(numbers2), id(numbers2))

print()
numbers3 = set(numbers2)
print(numbers3, type(numbers3), id(numbers3))

# Not OK
# We cannot convert list, set or tuple to dictionary or vice versa :(
# numbers5 = dict(numbers1) #error

