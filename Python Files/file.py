# Reading & Writing files in Python;
# Creating a file name file1.txt and writing some text.
file = open("C:\\users/Habib/PycharmProjects/python/Python Files/file1.txt", "w")
file.write("Hello Python!!!, You're so beautiful language.")
file.close()
print("File has written.")

# Reading a previous created file.
f = open("C:\\users/Habib/PycharmProjects/python/Python Files/joke.txt", "r")
print(f.read())
f.close()


