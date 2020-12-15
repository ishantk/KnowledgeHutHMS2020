john = {"fionna", "lee", "mike", "kia", "joe", "sia"}
jack = {"ben", "leo", "mike", "kia", "harry"}
dave = {"mike", "kia", "sia"}

print(john, type(john), len(john))
print(jack, type(jack), len(jack))
print(dave, type(dave), len(dave))

S1 = john | jack    # Union
S2 = john & jack    # Intersection
S3 = john - jack    # Difference

print("Union of John and Jack:", S1)
print("Intersection of John and Jack:", S2)
print("Difference of John and Jack:", S3)

S1 = john.union(jack)
S2 = john.intersection(jack)
S3 = john.difference(jack)

print("Union of John and Jack:", S1)
print("Intersection of John and Jack:", S2)
print("Difference of John and Jack:", S3)

# Membership Testing
print("kia" in john)

for friend in john:
    print(friend)

print(dave.issubset(john))
print(john.issuperset(dave))

set1 = {10, 20, 30, 40, 50}
set1.add(90)
set1.add(110)
set1.add(30)
set1.add(50)

print("set1:", set1)

set1.remove(90)
print("set1 now is:", set1)

# set1.clear()
# print("set1 after clear is:", set1)

list1 = list(set1)
print(list1, type(list1))

string_set = str(set1)
print(string_set, type(string_set))
print(string_set[0])
print(string_set[0:5])