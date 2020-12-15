"""
    Operations on Sequence String
"""
name = "John Watson"
another_name = "John Watson"

print(name, type(name), id(name))
print(another_name, type(another_name), id(another_name))

print(len(name))
print(min(name))
print(max(name))


# 1. Concatenation
family_name = name+" "+"Walter"
print("family_name:", family_name)
print()

# 2. Repetition
print(name*2)

# 3. Membership Testing
email = "john@example.com"
if "@" in email and "." in email:
    print("Valid Email")


# 4. Indexing
print(name[1])              # o
print(name[len(name)-1])    # n
print(name[-1])             # n
print(name[-3])             # s

# 5. Slicing
first_name = name[0:4]
print(first_name)

phone = "+91 99999 11111"
print("country code is:", phone[0:3])
print(phone[4:])
print(phone[:6])


# for i in range(len(name)):
#     print(name[i], end=" ~ ")

for alphabet in name:
    print(alphabet, end=" ^ ")

# print()
# print("hello", "hi", "bye", sep=":)")