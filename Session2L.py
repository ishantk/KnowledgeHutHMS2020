# More on Sequences

data = [1, 2, 3, 4, 5]

print("Length:", len(data))
print("Maximum:", max(data))
print("Minimum:", min(data))

# assignment: create your own functions to find length, max and min

# List Comprehensions
squared_numbers = [x**2 for x in data]
print("squared_numbers:", squared_numbers)

print()
product_prices = [1200, 300, 450, 890, 380]
sale_prices = [0.5*x for x in product_prices]

print("Original Prices:", product_prices)
print("Sale Prices:", sale_prices)

# assignment: explore list comprehensions to work with conditions
#             flat 50% off for products with price > 500

# explore for tuples :)
