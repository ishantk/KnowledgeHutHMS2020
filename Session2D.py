"""
    Function Execution Stack
    whenever we execute the function, in the background stack operation will come in action

"""

def compute_taxes(amount):
    taxes = 0.18 * amount
    total = amount + taxes
    return total

# y = m*x + c
def slope_of_line(m, x, c):
    y = m*x + c
    return y

"""
def main():
    print("main started")

    a = 10
    b = 20
    c = a+b
    print("c is:", c)

    print("Taxes are:", compute_taxes(2000))

    slope = slope_of_line(5, 2, 2)

    print("Slope of Line is:", slope)

    print("main finished")


if __name__ == "__main__":
    main()
"""

print("main started")

a = 10
b = 20
c = a + b
print("c is:", c)

print("Taxes are:", compute_taxes(2000))

slope = slope_of_line(5, 2, 2)

print("Slope of Line is:", slope)

print("main finished")