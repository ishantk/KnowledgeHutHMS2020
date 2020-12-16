# we can import modules with import keyword
"""
import Session3I

print("1. This is Session3J.py")
print("1. Session3J.py name is:", __name__)

print(Session3I.name)

Session3I.add(10, 20)

o_ref = Session3I.Order(201, 2500, "fionna@example.com")
o_ref.show()
"""

"""
import Session3I as I

print("1. This is Session3J.py")
print("1. Session3J.py name is:", __name__)

print(I.name)

I.add(10, 20)
o_ref = I.Order(201, 2500, "fionna@example.com")
o_ref.show()
"""

# from Session3I import name
# from Session3I import Order

# from Session3I import name, Order
from Session3I import *

print(name)
add(10, 20)
o_ref = Order(201, 2500, "fionna@example.com")
o_ref.show()

# execute the main as well
main()