# *
# **
# ***
# ****

"""n = 5
for i in range(n):
    for j in range (i):
        print("*",end="")
    print()"""

# 1
# 22
# 333
# 4444

"""n = 5
for i in range (n):
    for j in range(i):
        print(i,end="")
    print()"""
# A 
# BB
# CCC
# DDDD
# EEEEE

"""n = 6
ch = 'A'
for i in range (1,n):
    for j in range(i):
        print(ch,end="")
    ch = chr(ord(ch)+1)
    print()"""

# 1
# 21
# 321
# 4321

"""n = 4
for i in range(1,n+1):
    for j in range (i,0,-1):
        print(j,end="")
    print()"""

# 1
# 23
# 456
# 78910

"""n = 4
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end="")
        num+=1
    print()"""