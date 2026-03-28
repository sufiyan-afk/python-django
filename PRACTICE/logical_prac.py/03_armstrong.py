# find number is armstrong or not
n = 153
temp = n
sum = 0

while n >0:
    rem = n % 10   
    n = n // 10
    sum = sum + pow(rem,3)
    print(sum)
print(sum)

if temp == sum :
    print("armstrong number")
else :
    print("not armstrong number")
