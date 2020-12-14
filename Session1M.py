"""
    Bubble Sorting

    Input :  60, 12, 24, 18, 80  | Not Sorted
    Output:  12, 18, 24, 60, 80

    i:0
    0th iteration   60, 12, 24, 18, 80

                    j: 0, 1, 2, 3, 4
                    0.0 swapped 12 and 60
                        12, 60, 24, 18, 80
                    0.1 swapped 24 and 60
                        12, 24, 60, 18, 80
                    0.2 swapped 18 and 60
                        12, 24, 18, 60, 80
                    0.3 swap nothing
                        12, 24, 18, 60, 80
                    0.4 here data is sorted with 1st iteration

    i:1
    1st Iteration
                    12, 24, 18, 60
    i:2
    2nd Iteration
                     12, 24, 18
                     .
                     ...
                     ......
"""

# data = (60, 12, 24, 18, 80)
data = [60, 12, 24, 18, 80] # List in Python
# print(data, type(data)) # List is MUTABLE

print("ORIGINAL DATA IS:", data)

# Manipulation in List is Supported :)
# data[0] = 101
# print(data)
n = len(data)
for i in range(0, n): # 0, 1, 2, 3, 4
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            # swap the elements
            data[j], data[j+1] = data[j+1], data[j]

print("SORTED DATA IS:", data)