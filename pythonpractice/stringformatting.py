# So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings within strings.
#  String formatting uses a string's format method to substitute a number of arguments in the string.
# Example:
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#Example:
print("{0}{1}{0}".format("abra", "cad"))


# String formatting can also be done with named arguments.
# Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)


# The .format() method provides an easy way to format strings.
# Take as input a name and an age, and generate the output "name is age years old".
name= "ad"
age = 4
a = "{0} is {1} years old".format(name, age)
print(a)

#What is the result of this code?
str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)