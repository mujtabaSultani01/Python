"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
modifying its structure.
Let's first understand the need of python decorators.
See the following example having two functions which calculate the square and cube of an array:
This example has couple of problems: 1) if we have complex software program, and we have almost 100 function, so it's
difficult to write start and end statements for each function, and it will reduce our code readability. 2) We have
print logic inside each function which display the taken time, so it is not a better way.
"""

import time


def calculate_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("Total square_calculation takes ", (end - start) * 1000, " Mil seconds.")
    return result


def calculate_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    print("Total cube_calculation takes ", (end - start) * 1000, "Mil seconds.")
    return result


array = range(1, 100000)
square = calculate_square(array)
cube = calculate_cube(array)

# Using decorator concept, we just define @time_it at the beginning of each function, and it will calculate the time.

