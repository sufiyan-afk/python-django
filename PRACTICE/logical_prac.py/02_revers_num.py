# reverse the number and count digits
n = int(input("enter a number:"))
rev = 0
count = 0
sum = 0

while n >0:
    rem = n % 10              #reminder finding for reversing
    n = n // 10               # removing last digit for next iteration reversing
    count += 1                # for counting digits
    rev = (rev*10)+rem        # for reversing number
print(rev)                    # print reverse number
print(count)                  #print number of digits



