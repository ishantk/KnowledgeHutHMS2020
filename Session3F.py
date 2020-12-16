# r -> to read the file
file = open("Session3E.py", "r")

"""
# read line by line
line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

"""

# read all lines at once as list
"""
count = 0
lines = file.readlines()
print(type(lines))
for line in lines:
    print(line)
    if "def" in line:
        count += 1

print("{} functions found in Session3E.py".format(count))
"""

# read all at once
data = file.read()
print(data)
print("TYPE OF DATA:", type(data))

# once the data is read, we cannot re-read
data = file.read()
print("DATA:", data) # we wont see data again
# Hence, once data read, you need to open file again to re-read the data

file.close()