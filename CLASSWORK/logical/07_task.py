# # #fibonacci series 
# # length = 30 

# # a = 0 
# # b = 1

# # print (a , b , end = " ")

# # for i in range (length) :
# #     c= a + b
# #     print(c,end=" ")
# #     a = b
# #     b = c

# # #compounding 

# # day = int (input ("enter the day : "))
# sum = 1
# num = 1
# for i in range (2,32) :
#     num = num * 2
#     print(num)
#     sum = sum + num
# print(f"sum : {sum}")

#armstrong number
for i in range (100,1000) :
    result = 0 
    temp = i

    while i != 0 :
        rem = i % 10
        result = result + pow (rem,3)
      #  result = result * 10 + rem
        i = i // 10

    if temp == result : 
        print(temp,end = " ")
#num system finding 
# factorial using while loop
# finding length of number   







