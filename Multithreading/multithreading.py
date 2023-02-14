"""
Multithreading is the ability of a program or an operating system to enable more than one user at a time without
requiring multiple copies of the program running on the computer.
Multithreading can also handle multiple requests from the same user.

First of all we need to define threading model which is a standard model for multithreading.
Start() function start your thread
Join() function wait for other thread to be done.
"""


import time
import threading


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
t1 = threading.Thread(target=calculate_square, args=(arr,))
t2 = threading.Thread(target=calculate_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Calculating time: ", time.time() - t)

# So finally the process takes 1.25 seconds which is smaller than previous time (2.04).
