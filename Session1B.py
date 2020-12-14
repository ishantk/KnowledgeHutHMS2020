# Model
# Data Storage Container
# Container which will contain data, may be a single value or multiple values

# Create Statements -> To create a container
johns_age = 20

# Read or Print Statement
print("johns age is:", johns_age)
print("johns age HashCode is:", id(johns_age))

# johns_age which is variable is basically a Reference Variable
# it will hold the HashCode of data 20 :)
print()

jennies_age = 20
print("jennies age is:", jennies_age)
print("jennies age HashCode is:", id(jennies_age))

print()

# Update Statement
johns_age = 22
print("johns age now is:", johns_age)
print("johns age HashCode now is:", id(johns_age))

# reference copy
sias_age = jennies_age

print()

print("sias age is:", sias_age)
print("sias age HashCode is:", id(sias_age))

# Delete Statement
del jennies_age
# print("jennies age is:", jennies_age) # error
print("sias age is:", sias_age)

print()

print("Sias Age HashCode in Binary is:", bin(id(sias_age)))
print("Sias Age HashCode in Octal is:", oct(id(sias_age)))
print("Sias Age HashCode in Decimal is:", id(sias_age))
print("Sias Age HashCode in HexaDecimal is:", hex(id(sias_age)))