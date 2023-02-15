"""
Multiprocessing is a general term that can mean the dynamic assignment of a program to one of two or more computers
working in tandem or can involve multiple computers working on the same program at the same time (in parallel).
"""
import multiprocessing
import time


def calculate_square(numbers):
    for n in numbers:
        time.sleep(3)
        print("Square: " + str(n * n))


def calculate_cube(numbers):
    for n in numbers:
        time.sleep(3)
        print("Cube: " + str(n * n * n))


if __name__ == "__main__":
    arr = [2, 3, 4, 5]

    P1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    P2 = multiprocessing.Process(target=calculate_cube, args=(arr,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()

    print("The processes are completed.")
