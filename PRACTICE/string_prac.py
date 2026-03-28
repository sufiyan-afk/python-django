# wap to input user's first name & print its length 
"""name = input("enter your first name : ")

print(name)
print(len(name))
"""

# find first occurance of $

"""str = "hi $ is a us $ used for $ currency"
print(str.count("$"))
"""

str = "sufiyan"
for i in range(len(str)):
    print(str[i])
str[0]="S"   #error because string is immutable
