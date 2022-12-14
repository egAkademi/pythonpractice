""" List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. 
This returns a new list containing all the values in the old list between the indices. """

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.

list = ["a", "b", "c", "d"]
print(list[0:2])

# List slices can also have a third number, representing the step, to include only alternate values in the slice.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

# Negative values can be used in list slicing (and normal list indexing).
#  When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.
print(squares[::-1])

# Write a program that takes a list as input and outputs the last element of that list.
print(squares[-1])
print(squares[1])
print(squares[1:3])
print(squares[1:-3])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])