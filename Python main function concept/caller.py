# Now!, if we call 'area.py=>calculate_area()' from this file, then it will get error.
import area as a
result = a.calculate_area(3, 5)
print("Call from caller file.")
print("The area of triangle with (3,4) base and height is:", result)
