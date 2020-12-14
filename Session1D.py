"""
    Controller
        Operators           -> for computations
        Conditional Flows   -> for decisions and flows in program
        Iterations          -> doing tasks again and again

"""

# Operators
# Arithmetic -> Mathematical Computation

product_price = 1245.59
taxes = 0.18

final_price = product_price + product_price * taxes
print(final_price)
# +, -, *, **, /, //, %

number = 10
# result = number / 3   # floating point division
result = number // 3    # integral division
print(result)

base = 2
result = base ** 3      # exponential operation
print(result)

# Assignment Operators
# =, +=, -=, *=, /=, //=, **=, %=

price = 1450
price -= 100    # price = price - 100
print("price is:", price)

# Hashing -> Generating HashCodes for the data
buckets = 10
data = 54359

hash_code = data % buckets
print("HashCode for", data, "is:", hash_code)
# HashCode is 9
# means 54359 in the memory goes in bucket number 9

