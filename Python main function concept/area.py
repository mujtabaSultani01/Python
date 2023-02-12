"""
As we know when we write C or Java program, it should be starts from main function.
Similarly, in Python __name__ is a free defined variable which set to main, and 'if __name__ == __main__' is used
an entry point for any python program.
So, now the question is, when the value of __name__ is similar with __main__?
the answer is, when you directly access the file where we have __name__ == __main, then they're similar. but when we
access the file from other file it will be not similar and will get error.
"""


def calculate_area(base, height):
    print("__name__", __name__)
    return 1 / 2 * (base * height)


if __name__ == "__main__":
    resu = calculate_area(4, 7)
    print("The area of tringle with (4,7) base and height is: ", resu)
