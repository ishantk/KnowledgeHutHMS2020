# Recursion: Function Executing Itself Again and Again

# for i in range(1, 11):
#     print("i is:", i)


def print_number(number):

    if number > 5:
        return

    print("number is:", number)
    number += 1

    print_number(number)    # executing function from the function again
    # return


print("main started")

n = 1
print_number(n)

data = 100
print("data is:", data)

print("main finished")