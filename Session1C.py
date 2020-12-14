# Single Value Containers
instagram_id = "auribises"
print("instagram id is:", instagram_id)
print("HashCode of instagram_id is:", id(instagram_id))
print("Type of instagram_id is:", type(instagram_id))

age = 10
print("Type of age is:", type(age))

pi = 3.14
print("Type of pi is:", type(pi))

print()

# Multi Value Container
# Tuple -> MVC i.e. contains lot of data :)
# Homogeneous Multi Value Container
followers = "john", "jennie", "jim", "jack", "joe"
print("Followers is:", followers)
print("Followers HashCode is:", id(followers))
print("Followers Type is:", type(followers))

print("followers[0] is:", followers[0])
print("followers[0] HashCode is:", id(followers[0]))

print()

# Hetrogeneous Multi Value Container
data = "john", 10, 3.3, "sia"
print(data)
print(type(data))

# Limitation on Tuple or Feature of Tuple
# we can not modify tuple after it is created :)
# Tuple is IMMUTABLE, once created cannot be modified :)
# followers[1] = "jennie watson"
# del followers[0] error