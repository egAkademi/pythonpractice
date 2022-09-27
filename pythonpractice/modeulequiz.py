def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))


""" You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value. """
celsius = 36

def conv(c):
    #your code goes here
    return (9/5)*c + 32

fahrenheit = conv(celsius)
print(fahrenheit)
