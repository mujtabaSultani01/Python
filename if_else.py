
# Debugging is the process to execute code line by line and do analysis on what's going on at each step.
number = input("Enter a number: ")
number = int(number)

# print("You entered: ", number)
if number%2 == 0:
    print("You entered even number.")
else:
    print("You entered odd number.")


Male_class = ["Faisal", "Fawad", "Fayez", "Faizan"]
Female_class = ["Marwa", "Safa", "Khadija", "Sana"]

stu_name = input("Enter a student name: ")

if stu_name in Male_class:
    print("He is founded in the Male class.")
elif stu_name in Female_class:
    print("She is founded in Femal class.")
else:
    print("He is not our student.")
