#types of conditionals statements
#1. if statement
#2. if-else statement
#3. elif statement
#4. nested if statement


marks=int(input("enter your marks:"))
if marks>=91 and marks<=100:
    print("you got A grade")
elif marks>=71 and marks<=90:
    print("you got B grade")
elif marks>=51 and marks<=70:
    print("you got C grade")
elif marks>=35 and marks<=50:
    print("you got D grade")
elif marks>=0 and marks<=34:
    print("you got E grade")
else:
    print("invalid marks")

#match case statement is a new conditional statement introduced in python 3.10\
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

option=input("enter the operation you want to perform (+,-,*,/):")

match option:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case _:
        print("invalid option")