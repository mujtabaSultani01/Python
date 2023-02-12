import calculate

# if the file you want to import is not in the same directory, if the file is in the subdirectory (modules), then
# import it as: modules.calculate. if the file is outside the directory, then use system path ("C:\...\calculate").

base = input("Enter the tringle base: ")
base = int(base)

height = input("Enter the tringle height: ")
height = int(height)

length = input("Enter the length of square: ")
length = int(length)

tringle_area = calculate.calculate_tringle_area(base, height)
square_area = calculate.calculate_square_eara(length)

print("The area of tringle with base=4 and height=7 is equal to: ", tringle_area)
print("The eara of square wiht length=5 is equal to: ", square_area)

