
#You can raise exceptions by using the raise statement.

try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

try:
    num = 5 / 0
except:
    print("An error occurred")
    raise