print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Lucky CashBacks")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

cash_backs = [100, 200, 12, 35, 50, 60, 80, 500, 10, 40]
lucky_number = 0
try:
    lucky_number = int(input("Enter Your Lucky Number: "))
    print("You have Earned {} amount as CashBack".format(cash_backs[lucky_number]))
# except ValueError as ref:
#     print("Sorry, No CashBack Earned")
# except IndexError as ref:
#     print("Sorry, No CashBack Earned")
except Exception as e:
    print("Something Went Wrong:", e)
    # print(e.with_traceback())
finally:
    print("Be Happy, Some Additional CashBack for You: ", lucky_number*2)

print("Thank You For Playing Lucky Numbers with Us :)")

"""
    class Exception:
        pass
        
    class ValueError(Exception):
        pass 
        
    class IndexError(Exception):
        pass      
"""