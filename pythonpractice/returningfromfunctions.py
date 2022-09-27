""" Certain functions, such as int or str, return a value that can be used later.
To do this for your defined functions, you can use the return statement. """

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

""" Once you return a value from a function, it immediately stops being executed. Any code after the return statement will never happen. """

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))


""" 
We are creating our own social network application and need to have a hashtag generator program.
Complete the program to output the input text starting with the hashtag (#).
Also, if the user entered several words, the program should delete the spaces between them.

Sample Input
code sleep eat repeat

Sample Output
#codesleepeatrepeat

Hint
You can use the replace() function to replace the spaces (" ") with empty strings (""). See how it works: """

s = "code sleep eat repeat"

def hashtagGen(text):
	#your code goes here
	s1 =  s.replace(" ", "")	
	return "#" + s1

print(hashtagGen(s))


def shout(word):
   return word + "!"
speak = shout
output = speak("shout")
print(output)
