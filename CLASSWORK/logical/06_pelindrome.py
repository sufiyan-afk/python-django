number = 123454321
temp = number
sum = 0 
while number != 0:
    rem = number % 10
    sum = (sum*10)+rem
    number //= 10

if temp == sum:
    print("pelindrome")
else:
    print("not pelindrome")
