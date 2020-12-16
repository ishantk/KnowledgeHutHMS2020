# Lambda Expression


def area_of_circle(radius=1.0):
    # area = 3.14 * radius * radius
    return 3.14 * radius * radius


# Reference Copy for Function
a_ref = area_of_circle

print("area_of_circle is:", area_of_circle)
print("a_ref is:", a_ref)

print("Area of Circle with Radius 15 is:", area_of_circle(15))
print("Area of Circle with Radius 5 is:", a_ref(5))

# Lambda: Where we solve single expression
#         generally a single unit of work

l_ref1 = lambda radius=1.0: 3.14 * radius * radius
print("l_ref1 is:", l_ref1)

print("Area of Circle with Radius 25 is:", l_ref1(radius=25))

l_ref2 = lambda x, y: x**y
print("2 power 3 is:", l_ref2(2, 3))

l_ref3 = lambda x=int(input("Enter X: ")), y=int(input("Enter Y: ")): l_ref1(x) + l_ref2(x, y)
# print(l_ref3())
result = l_ref3()
print("Result is:", result)



