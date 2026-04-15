operator = input("enter an operator (+ - * / )")
num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)

else:
    print("invalid operator")
