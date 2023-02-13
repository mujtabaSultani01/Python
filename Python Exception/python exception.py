"""
Exception are errors detected at the time of program execution.
Simple exception examples are: 1/0, 'abcd' + 50; => in this situation it will generate exception & will terminate
the program execution.
"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


try:
    div_res = int(num1) / int(num2)
except Exception as e:
    print("Exception occurred:", e)
    div_res = None
    print("The division result is: ", div_res)

# Or we can prevent the divideByZero exception in a better way (specific way):

try:
    div_res = int(num1)/int(num2)
except ZeroDivisionError as e:
    # print("DivideByZero exception occurred:", e)
    print("DivideByZero Exception occurred.")
    div_res = None
    print("The division result is: ", div_res)

# We can also prevent multiple exceptions at the same time:

# try:
 #   div_res = num1 / int(num2)
# except ZeroDivisionError as e:
  #  print("DivideByZero Exception occurred.")
   # div_res = None
# except TypeError as e:
  #  print("TypeError exception occurred.")
   # div_res = None
    # print("The division result is: ", div_res)




