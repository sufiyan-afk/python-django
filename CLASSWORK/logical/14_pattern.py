# *****
# *****
# *****
# *****
# *****
"""
for i in range(5):
    for i in range(5):
        print("*",end="")
    print()

# *
# **
# ***
# ****
# *****

lines = 5
for i in range(lines):
    for j in range(i+1):
        print("*",end="")
    print()

#for i in range(5):
#     print((i+1)*"*")

# *****
# ****
# ***
# **
# *

lines = 7
for i in range(lines):
    for j in range(lines - i):
        print("*",end="")
    print()

#     *
#    **
#   ***
#  ****
# *****

lines = 6
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j+1):
        print("*",end="")
    print()

# *****
#  ****
#   ***
#    **
#     *


lines = 6
for i in range(lines):
    for k in range(i):
        print(" ",end="")
    for j in range(lines-i):
        print("*",end="")
    print()

#    *
#   * *
#  * * *
# * * * *


lines = 5
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j+1):
        print("* ",end="")
    print()


#       *
#      ***
#     *****
#    *******
#   *********


lines = 5
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j*2+1):
        print("*",end="")
    print()
"""

# homework
#       *
#      ***
#     *****  #diamond
#      ***
#       *

"""
n = int(input("enter a number : "))

for i in range (1,n+1):

    for j in range(n-i):
        print(" ",end ="")
    for j in range(2*i-1):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
    """

# hollow diamond 
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

"""
n=5

#top part
for i in range (n):
    #;left spaces
    for j in range (n-i-1):
        print(" ",end="")
        #first star
    print("*",end="")

#for middle spaces (hollow)
    if i > 0:
        #spaces
        for j in range(2*i-1):
            print(" ",end="")
        print("*",end="")
    print()  #for new line

# for bottom part
for i in range (n-1):
    #for left spaces
    for j in range(i+1):
        print(" ",end="")
    print("*",end="")
    #for middle spaces (hollow)
    if i<n-2:
        for i in range(2*(n-i-2)-1):
            print(" ",end="")
        print("*",end="")
    print()
"""
# lines = 5
# count = 0
# for i in range(lines):
#     for j in range(i):
#         print(count+1,end="")
#         count+=1
#     print()

# lines = 5
# count = 0
# for i in range(lines):
#     for j in range(i):
#         print(j+1,end="")
#         count+=1
#     print()

# lines = 5
# count = 0
# for i in range(lines,0,-1):
#     for j in range(i,lines+1):
#         print(j,end="")
    
#     print()

lines = 5
count = 0
for i in range(lines):
    for j in range(i+1):
        print((i+j)%2,end="")
    print()

