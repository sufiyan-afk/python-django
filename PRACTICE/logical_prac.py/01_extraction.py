# extraction of digits
n = int(input("enter a 4 digit number"))
count = 0
while n>0:
    lastdigit = n % 10
    print(lastdigit)
    n=n//10
    count += 1
print(f"total digits : {count}")



