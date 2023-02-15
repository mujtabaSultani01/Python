"""
Now let's instead printing the result (calculate_square_cube.py_, store the result in global variable:
"""
import multiprocessing

import Multiprocessing
import time

square_result = []


def calculate_square(numbers):
    global square_result
    for n in numbers:
        print("Square: " + str(n * n))
        square_result.append(n * n)
        print("Within the process: " + str(square_result))


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    P1 = multiprocessing.Process(target=calculate_square, args=(arr,))

    P1.start()
    P1.join()

    print("Result: " + str(square_result))  # This won't give you the output. Cause every process has its own address
    # space (virtual memory). This issue is covered in data_share.py file.
    print("Let's done it...")
