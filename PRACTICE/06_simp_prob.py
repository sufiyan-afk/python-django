# #conditionals statements

# light = input("light : ")

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("wait")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")

# A = int(input("A : "))
# G = input("m/f : ")

# if((A == 1 or A == 2) and G == "m"):
#     print("fee is 100")
# elif((A == 3 or A == 4) and G == "f"):
#     print("fee is 200")
# elif((A == 5 or A == 6)and G == "m"):
#     print("fee is 300")
# else:
#     print("no fee")

#ternary operator
# food = input("food : ")
# eat = "yes" if food == "cake" else "no"
# print(eat)

# food = input ("food")
# print("sweet") if food == "cake" or food == "jalebi" else print ("not sweet")


#clever if statement 
#for tax management

# sal = int(input("salary : "))
# tax = sal * (0.1,0.2) [sal <= 50000]
# print(tax)

#calculate simple interest

# p = float (input("percentage : "))
# r = float (input("rate : "))
# t = float (input("time : "))
# si = (p*r*t)/100
# print(si)

# num1 = int (input("enter first number : "))
# num2 = int (input("enter second number : "))
# sum = num1 + num2
# print(f"sum of two numbers is {sum}")

# side = int (input ("enter side of square : "))
# area = side *side 
# print(f"area of square is {area}")

# num1 = float (input ("enter first number : "))
# num2 = float (input ("enter second number :"))
# average = (num1 + num2) / 2
# print (f"average of two floating numbers is {average}")

a = int (input ("enter first :"))
b = int (input ("second number : "))
if(a >= b) :
    print("true")
else:
    print("false")