# Finally is something which could be used for cleaning...
def process_file():
    try:
        file = open("C:\\users/Habib/PycharmProjects/python/Python Files/f.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("Inside exception...")
    finally:
        print("Cleaning up the file.")
        file.close()
process_file()
# Now as we see the output, we have exception but using finally we clan close the file.

