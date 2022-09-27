fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
num = 5
#your code goes here
print(len(fruits))
print(fruits[num])

if 0<=num<=7:
    print(str(fruits[num]))
elif num<0 or num>7:
    print("Wrong number")

nums = [5, 4, 3, 2, 1]
print(nums[1])

list = [2,]
print(len(list))
print(list)


number = 0
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

if number in things:
    print("bingo")


str = "Hello world!"
print(str[6])