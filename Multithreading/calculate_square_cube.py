"""
Multithreading is the ability of a program or an operating system to enable more than one user at a time without
requiring multiple copies of the program running on the computer.
Multithreading can also handle multiple requests from the same user.
"""
import time


def calculate_square(numbers):
    print("Calculating square of given array.")
    for number in numbers:
        time.sleep(0.2)
        print("Square: ", number * number)


def calculate_cube(numbers):
    print("Calculating cube of given array.")
    for number in numbers:
        time.sleep(0.3)
        print("Cube: ", number * number * number)


arr = [2, 3, 4, 5]

t = time.time()
calculate_square(arr)
calculate_cube(arr)
print("Calculating time: ", time.time() - t)

# So now let's see, how we improve the execution time which we had in upper example (2.04), check multithreading.py
