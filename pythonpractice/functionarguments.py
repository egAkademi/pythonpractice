password = "John894"
repeat = "John894"

def validate(text1, text2):
	#your code goes here
	if (text1==text2):
		print("Correct")
	else:
		print("Wrong")

validate(password,repeat)

#Fill in the blanks to pass the function "square" as an argument to the function "test":

def square(x):
	return x * x

def test(func,x):
	print(func(x))

test(square,42)