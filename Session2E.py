a = 10

def square():
    global a # -> we are telling square to use a which is defined outside as global
    a = 12
    a = a * a
    print("2. a is:", a)

print("1. a is:", a)
square()
print("3. a is:", a)


