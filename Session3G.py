file = open("customers.csv", "r")

# tell will give us the current position of cursor in the file
print("Cursor Position:", file.tell())

# move the cursor to 10th index
file.seek(10)

# Just read 15 characters
data = file.read(15)
print(data)

print("Cursor Position Now:", file.tell())
