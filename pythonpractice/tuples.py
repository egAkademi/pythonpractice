#Fill in the blanks to create a list, dictionary, and tuple:
# list

list = [
"one", "two"
]

# dictionary 

dict = {
1:"one", 2:"two"
}

# tuple 

tp = ( "one", "two" )
print(tp[0])
#Tuples can be created without the parentheses, by just separating the values with commas.
tpp = "one","two"
print(tpp[0])
#Tuples are faster than lists, but they cannot be changed.


""" You are given coordinates of 2 points and need to find the straight line distance between them.

The coordinates are provided in a tuple, for example:
The first value represents the x coordinate, while the second value represents the y coordinate of the point p.

Complete the provided code to calculate and output the distance between the two given points.
The linear distance is the square root of the square of the horizontal distance plus the square of the vertical distance between two points.
The math.sqrt() function can be used to calculate the square root. """
import math

p1 = (23, -88)
p2 = (6, 42)

res = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) )
print(res)
