""" List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
For example, we can do the following: """

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

# A list of even numbers between 0 and 10
nums = [i*2 for i in range(10)]
print(nums)

# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# Create a list of multiples of 3 from 0 to 20.

a= [i for i in range(20) if i %3 ==0]
print(a)

""" Trying to create a list in a very extensive range will result in a MemoryError.
This code shows an example where the list comprehension runs out of memory. """

#even = [2*i for i in range(10**100)]

#hem 3 hem 5 e bölünen 100 ün altındaki sayıları veren liste:
b = [i for i in range(100) if i % 15 == 0]
print(b)

#5 ila 9 aralığında 10 ile çarpılan sayıların bir listesini oluşturmak için
c=[x*10 for x in range(5,9)]
print(c)