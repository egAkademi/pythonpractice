# To write to files you use the write method, which writes a string to the file.
# For example:

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

# when a file is opened in write mode, the file's existing content is deleted.

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()


names = ["John", "Oscar", "Jacob"]
file = open("names.txt", "w+")
#write down the names into the file
for i in names:
    file.write(i+ "\n")
file.close()

file= open("names.txt", "r")
#output the content of file in console
print(file.read())

file.close()
