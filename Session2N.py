# Dictionary
menu = {
    "burger": 100,
    "fries": 50,
    "noodles": 150,
    "pizza": 100,
    "samosa": 20
}

print(menu)
print(type(menu))

# Update Operation
menu["fries"] = 80

# Read Operation
print(menu["fries"])
print(menu["pizza"])

cart = []
choice = "yes"
total = 0

while choice == "yes":
    item = input("Enter Food Item: ")
    cart.append(item)
    total += menu[item]

    choice = input("Would you like to add more items in cart (yes/no): ")

if total >= 150:
    print("We will give some complimentry items :)")
    cart.extend(["nuggets", "coke"]) # extend will concatenate in the same list itself

print("Cart[{}]:".format(len(cart)))
print(cart)
print("Amount to Pay:", total)

# assignment: explore session2k on dictionary