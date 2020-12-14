# Functions
# function is a block of statements which is used again and again in program
# we can create it and use it whenever we wish to use it
# it can have inputs
# it can also return the data as result for some computations


product_prices = 4532, 5431, 43331, 1234, 8765
active_covid_cases = 201, 125, 545, 332, 112, 564, 345, 865, 331
cricket_score = 205, 120, 90, 180, 210

# Find the maximum product product price
# Find the maximum active cases for covid
# Find the maximum cricket score for the team

def max_in_tuple(data):

    max = data[0]

    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]

    return max

"""
max = product_prices[0]
for i in range(1, len(product_prices)):
    if product_prices[i] > max:
        max = product_prices[i]

print("max in product_prices is:", max)

print()

max = active_covid_cases[0]
for i in range(1, len(active_covid_cases)):
    if active_covid_cases[i] > max:
        max = active_covid_cases[i]

print("max in active_covid_cases is:", max)

print()
max = cricket_score[0]
for i in range(1, len(cricket_score)):
    if cricket_score[i] > max:
        max = cricket_score[i]

print("max in cricket_score is:", max)
"""

"""
max_product_price = max_in_tuple(product_prices)
max_covid_cases = max_in_tuple(active_covid_cases)
max_cricket_score = max_in_tuple(cricket_score)

print("max_product_price:", max_product_price)
print("max_covid_cases:", max_covid_cases)
print("max_cricket_score:", max_cricket_score)
"""

"""
print("max_product_price:", max_in_tuple(product_prices))
print("max_covid_cases:", max_in_tuple(active_covid_cases))
print("max_cricket_score:", max_in_tuple(cricket_score))
"""

print("max_product_price:", max(product_prices))
print("max_covid_cases:", max(active_covid_cases))
print("max_cricket_score:", max(cricket_score))
