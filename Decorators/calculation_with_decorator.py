"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
modifying its structure.
"""

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 10000) + " Mil seconds.")

    return wrapper


@time_it
def calculate_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


@time_it
def calculate_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


@time_it
def calculate_quadrupled(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number*number)
    return result


array = range(1, 100000)
calculate_square(array)
calculate_cube(array)
calculate_quadrupled(array)
