"""
The key difference between Multithreading and Multiprocessing is, in Multithreading you will see the result being fill
outside the function but in Multiprocessing you won't see the result outside the function.
So let's solve the problem and share data between two processes. For that we use Shared Memory concept.
There are two ways using shared memory: 1) value 2) array
Let's first see the array and then value:
"""

import multiprocessing


def calculate_square(numbers, res):
    for idx, n in enumerate(numbers):
        res[idx] = n*n


if __name__ == "__main__":
    array = [2, 3, 4, 5]
    result = multiprocessing.Array('i', 4)
    P1 = multiprocessing.Process(target=calculate_square, args=(array, result))

    P1.start()
    P1.join()

    print("Result: " + str(result[:]))
    print("Let's done it...")

# Let's see data sharing concept using vlue:


def calculate_square1(numbers, resu, va):
    va.value = 3.10
    for idx, n in enumerate(numbers):
        resu[idx] = n*n


if __name__ == "__main__":
    array = [2, 3, 4, 5]
    result = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    P1 = multiprocessing.Process(target=calculate_square, args=(array, result))

    P1.start()
    P1.join()

    print("Result: " + str(result[:]))
    print("Value: " + str(v.value))
    print("Let's done it...")
