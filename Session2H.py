"""
    Value VS Reference in Functions
"""

"""

# PASS BY VALUE :)
def square_of_number(number):
    print("number is:", number)      # 10
    number = number * number
    print("number now is:", number)  # 100
        


def main():
    num = 10
    print("num is:", num)       # 10
    square_of_number(num)
    print("num now is:", num)   # 10


if __name__ == '__main__':
    main()

"""


# PASS BY Reference :)
def square_of_numbers(numbers):
    print("numbers is:", numbers)  # 10, 20, 30, 40, 50

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

    print("numbers now is:", numbers)  # 100 400 .....


def main():
    nums = [10, 20, 30, 40, 50]
    print("nums is:", nums)  # 10, 20, 30, 40, 50
    square_of_numbers(nums)
    print("nums now is:", nums)  #  100 400 .....


if __name__ == '__main__':
    main()
