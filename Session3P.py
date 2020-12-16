"""
    Map Filter and Reduce
    Using built in function in Python

"""

product_prices = [1200, 3500, 3799, 2200, 1801]

# def discount(amount):
#     return amount - amount * 0.20

# Lambdas are Functions with Single Expression
l_ref1 = lambda amount: amount - amount*0.20

# for price in product_prices:
#     print(l_ref1(price))

# map -> map is a bult in function in python
# it maps the data with lambda or functio

result = map(l_ref1, product_prices)
print(result, type(result))

reduced_prices = list(result)
print("Reduced Prices are:", reduced_prices)

print()

numbers = list(range(10, 21))
numbers2 = list(range(30, 41))
print(numbers)

l1 = lambda num : num%2==0  # even number
l2 = lambda num : num%2!=0  # odd number

print(list(map(l1, numbers)))
print(list(map(l2, numbers)))

print()

print(list(filter(l1, numbers)))
print(list(filter(l2, numbers)))

print()

l3 = lambda X, Y : X + Y
print(l3(numbers, numbers2))

print()

from functools import reduce
nums = [10, 20, 30, 40, 50]
result = reduce(l3, nums)
print("result is:", result)





