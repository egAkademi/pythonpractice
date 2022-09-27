#range() işlevi bir dizi sayı döndürür .

numbers = list(range(10))
print(numbers)

nums = list(range(5))
print(nums[4])

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

nums = list(range(5, 8))
print(len(nums))

numbers = list(range(5, 20, 2))
print(numbers)

nums = list(range(3, 15, 3))
print(nums[2])

#Bir web sitesi için bir tarih seçici yapıyorsunuz ve belirli bir dönemde tüm yılları çıkarmanız gerekiyor.
#Girdi olarak iki tamsayı alan ve iki girdi arasındaki sayı aralığını liste olarak veren bir program yazın.
#Çıkış sırası, ilk giriş numarası ile başlamalı ve ikinci giriş numarası ile bitmeden bitmelidir.

# a = int(input())
# b = int(input())
a = 2015
b = 2022
#your code goes here
numbers = list(range(a,b))
print(numbers)