# Break and Continue in Loops

employees = 101, 201, 451, 221, 675, 432, 123, 567
employee_id = int(input("Enter Employee Id to be Found: "))

"""
for i in range(len(employees)):
    print("Matching ", employee_id, "with", employees[i])
    if employee_id == employees[i]:
        print(employee_id, "Found :)")
        # terminate the loop to be executed further
        break
"""

for i in range(len(employees)):

    if employee_id != employees[i]:
        continue
        # skip the statements below in the loop and take it to next iteration

    print("Match Found For", employee_id)