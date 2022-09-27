""" You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the open function. """

# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.

# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

myfile = open("Kitap1.xlsx")


# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")