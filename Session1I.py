# Loops

print("==while loop==")

idx = 1
while idx <= 10:
    print("idx is:", idx)
    # idx += 1
    idx += 2

print("we dont have do while loops in python :(")

print("==for loop==")

# for i in range(1, 11):
# for i in range(1, 11, 1):
for i in range(1, 11, 2):
    print("i is:", i)

print()

print("==nested loop==")
for i in range(1, 6): # 1, 2, 3, 4, 5
    print("i is:", i)

    # internal loop
    # it will work i times the j number of times for the outer loop
    for j in range(1, 4): # 1, 2, 3
        print(j, end=" ")

    print()