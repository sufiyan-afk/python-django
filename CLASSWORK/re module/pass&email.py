import re
# number = input("enter number")
# k = re.match("^[0-9]{10}$",number)
# if k is None:
#     print("Invalid number")
# else:
#     print(number)

email = input("enter your email")
l = re.match("^[a-z0-9_-]+@[a-z0-9]+\\.[a-z]{2,5}$",email)
if l is None:
    print("invalid email ! please enter a valid email")
else:
    print(email)
