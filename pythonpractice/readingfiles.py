# The contents of a file that has been opened in text mode can be read using the read method.

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

# To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()


file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

file = open("filename.txt", "r")
print(file.readlines())
file.close()

file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 