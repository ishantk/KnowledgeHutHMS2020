"""
    Built In Modules
"""

# print(help("id"))
# print(help("print"))
# print(help("modules"))

# import math as m
import math
import os
import random
import sys
import statistics
import time
import datetime

print("MATH MODULE")
print(math.sqrt(16.0))
print(math.pi)
print(math.e)
print(math.sin(0.5))
print(math.sin(0.5))
print(math.cos(0.5))
print(math.tan(0.5))

print(math.log10(100))
print(math.pow(2, 3))

print()

bill_amount = 5.4
print(math.ceil(bill_amount))
print(math.floor(bill_amount))

print()
print("OS MODULE")
# os.mkdir("/Users/ishantkumar/Downloads/mypyapp")
# print("Directory Created")

# print(os.getcwd())
# os.chdir("/Users/ishantkumar/Downloads/mypyapp")
# print(os.getcwd())

# os.rmdir("/Users/ishantkumar/Downloads/mypyapp")

# print(os.listdir("/Users/ishantkumar/Downloads"))

for file in os.listdir("/Users/ishantkumar/Downloads"):
    if file.endswith(".docx") or file.endswith(".pdf"):
        print(file)

print()
print("RANDOM MODULE")
number = random.random()
print(number)

otp = random.randint(1001, 9999)
print("OTP is:", otp)

otp = random.randrange(1000, 5000, 10)
print("OTP now is:", otp)

name = "johnwatson"
print(random.choice(name))

numbers = [10, 12, 15, 19, 55, 33, 21, 50, 99]
print(random.choice(numbers))
print("Original Numbers:", numbers)
random.shuffle(numbers)
print("Shuffled Numbers:", numbers)

# sys.exit()
print(sys.maxsize)
print(sys.path)
print(sys.version)

# argv[1] and argv[2] are suppose to be given at command line :)
# print("This is hello for {}".format(sys.argv[1]))
# print("Good to know that your are {} years old".format(sys.argv[2]))

print(statistics.mean(numbers))
print(statistics.median(numbers))
print(statistics.mode([2, 5, 3, 2]))
print(statistics.stdev(numbers))

print(time.time())

t_ref = time.time()
tm_local = time.localtime(t_ref)
readable_time = time.asctime(tm_local)
print(readable_time)

# print(time.sleep(5))

# print(datetime.datetime().today())

print("Thank You :)")
