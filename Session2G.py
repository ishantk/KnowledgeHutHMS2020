"""
    Functions and their HashCodes
"""


def say_hello(name):
    print("Hello, {}. Good to Meet You".format(name))


say_hello("John")
say_hello("Fionna")

print("Lets Print say_hello")
print(say_hello, type(say_hello))
print("HashCode of say_hello is:", id(say_hello), hex(id(say_hello)))

# Reference Copy
# Alias Name to Functions :)
hello = say_hello
print("Lets Print hello")
print(hello, type(hello))

hello("Dave")
hello("Sia")


def say_hello(name1, name2):
    print("Hello {} and {}. Pleasure to Meet you".format(name1, name2))


print("Lets Print say_hello again after we re defined it")
print(say_hello, type(say_hello))

say_hello("Kia", "Sia")
hello("Joe")

# del hello
# hello("Harry")

print()

"""
def fun(input):
    input("George", "Harry")

fun(say_hello)
"""

