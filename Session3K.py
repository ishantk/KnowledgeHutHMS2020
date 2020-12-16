"""
# import pack.One
import pack.One as one
print("This is Session3K")

one.show()
one.add(10, 20)
c_ref = one.CA()
print("name is:", one.name)
"""

# from pack.One import *
from pack.One import name, add, CA
print(name)
add(10, 20)
c_ref = CA()