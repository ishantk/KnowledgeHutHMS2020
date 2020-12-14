# Conditional Operators
# ==, !=, >=, <=, <, >

# Logical Operators
# and or

# Membership Operators
# is, is not

cab_fare = 500
wallet = 70

print("Can i Book the Cab", (wallet >= cab_fare))

user_name = "john@example.com"
password = "pass123"

print("Authenticate Email:", (user_name == "john@example.com"))
print("Authenticate Password:", (password == "pass123"))

print("Authenticate User to Login:", (user_name == "john@example.com") and (password == "pass123"))

otp = 3027
# user_otp = input("Enter OTP: ") # by default everything read is String :)
user_otp = int(input("Enter OTP: "))
print("user_otp is:", user_otp, "and its type is:", type(user_otp))
# RULE: Data Entered by User in the Software is always read as String
#       Data to be displayed to User is always displayed as String

print("OTP Matched:", otp == user_otp)

internet_status = False
print("Can is Use Google Maps", internet_status, type(internet_status))

a = 10
print(a is 10)
print(a == 10)

name = "fionna"
print(name is "fionna")
print(name == "fionna")

print(name is not "john")
print(name != "john")

# assignment1: explore the difference between is and == :)
