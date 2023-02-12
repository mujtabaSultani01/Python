"""
Function is a block of code that performs a specific task:
if we want to add two persons expenses, so without using function we'll do it as follows:
"""
faisal_exp_list = [3000, 2300, 3200, 1400, 5000]
fawad_exp_list = [2000, 3200, 2000, 1200, 4000]
total = 0
for items in faisal_exp_list:
    total = total + items
print("Faisal total expenses is: ", total)

total = 0
for items in fawad_exp_list:
    total = total + items
print("Fawad total expense is: ", total)


# Now using function we'll do the sum much easily.
def calculate_exp(exp):
    total_exp = 0
    for item in exp:
        total_exp = total_exp + item
    return total_exp


faisal_expenses = calculate_exp(faisal_exp_list)
fawad_expenses = calculate_exp(fawad_exp_list)

print("Faisal total expenses is: ", faisal_expenses)
print("Fawad total expenses is: ", fawad_expenses)


# End of sum using function.

# let's have another example of adding two numbers:

def calculate_num(a, b):
    result = a + b
    print("Result of adding a and b is: ", result)


num1 = input("Enter the first number: ")
num1 = int(num1)

num2 = input("Enter the second number: ")
num2 = int(num2)

calculate_num(num1, num2)
