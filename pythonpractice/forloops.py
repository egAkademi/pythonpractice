words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)


list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        continue    


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#your code goes here
sum = 0
for i in list:
    sum+=i
print(sum)