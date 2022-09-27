try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")


try:
  print(1)
except:
  print(2)
finally:
  print(3)


coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = 8

try:
	
	print(str(coffee[choice]))
	#your code goes here
except:
	#and here
	print("Invalid number")
	
finally:
	#and finally here
	print("Have a good day")