""" Modules are pieces of code that other people have written to fulfill common tasks,
such as generating random numbers, performing mathematical operations, etc.

The basic way to use a module is to add import module_name at the top of your code, 
and then using module_name.var to access functions and values with the name var in the module.
For example, the following example uses the random module to generate random numbers: """

from cmath import cos
import random

for i in range(5):
    value = random.randint(1, 6)  #The code uses the randint function defined in the random module to print 5 random numbers in the range 1 to 6.
    print(value)

import math
num = 10
print (math.sqrt(num))

from math import sqrt , cos


import math as m
print(m.sqrt(25))