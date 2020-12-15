"""
    Strings
    Set
    Dictionary
"""

# restaurant_name = 'Johns Coffee Shop'
# restaurant_name = 'John's Coffee Shop' # error
# restaurant_name = 'John\'s Coffee Shop'
restaurant_name = "John's Coffee Shop"
print("restaurant_name:", restaurant_name)

# Raw Strings
# where escape sequences becomes part of data :)
quote = r'John\'s Coffe Shop Be Exceptional \n Work Hard'
print(quote)
print(type(quote))

# Multi Line String
message = """
This is a hello from your friend.
I hope you are doing good.
See you soon
"""

print(message)
print(type(message))