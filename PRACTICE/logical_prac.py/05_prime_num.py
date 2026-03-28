# n = int(input("enter the number : "))
# count = 0

# for i in range(1,n+1):
#     if n % i == 0:
#         count+=1
# if count == 2:
#     print("prime number")
# else:
#     print("not prime number")


#find prime numbers from 1 to 100
for k in range (1,101):
    n = k
    flag = 0
    for i in range(2,n):
        if n %i == 0:
            flag = 1
            break

    if flag == 0:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")