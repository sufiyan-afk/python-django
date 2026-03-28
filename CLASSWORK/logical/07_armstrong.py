number = 153
l = len(str(number))
temp = number
sum = 0
while number != 0:
    rem = number%10
    sum += pow(rem,l)
    number//=10

if temp == sum:
    print(f"{temp} is armstrong number")
else:
    print(f"{temp} is not armstrong")