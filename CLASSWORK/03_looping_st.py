# #types of looping statements
# #1. for loop
# #2. while loop
# #3. nested loop

# choice = 'y'
# while choice != 'n':
#     num1 = int(input("enter first number:"))
#     num2 = int(input("enter second number:"))

#     option = input("enter the operation you want to perform (+,-,*,/):")

#     match option:
#         case '+':
#             print(num1 + num2)
#         case '-':
#             print(num1 - num2)
#         case '*':
#             print(num1 * num2)
#         case '/':
#             print(num1 / num2)
#         case _:
#             print("invalid option")

#     choice = input("do you want to continue (y/n):")

# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))

# option=input("enter the operation you want to perform (+,-,*,/):")

# match option:
#     case '+':
#         print(num1+num2)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         print(num1/num2)
#     case _:
#         print("invalid option")


fruits = ['Apple','Banana','mango']

for fruit in fruits:
    if fruit == 'Banana':
        continue
    print(fruit)

    