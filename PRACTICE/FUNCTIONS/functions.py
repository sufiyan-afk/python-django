# basic addition of two numbers 



"""def add():      # made a function
    a = 8
    b = 10
    c = a + b
    print(c)

add()         # function calling without parameters
"""


'''def add(a,b):     #function defining
    """addtion function"""
    sum = a + b
    print(sum)
    return(sum)

add(3,4) # function calling with two parameters'''
"""
def average(a,b,c):
    avg = (a + b + c) / 3
    print(avg)
    return (avg)

average(1,2,3)
"""
"""
#default parameter : assigning a default value in parameter,which is used when no argument is passed

def mult(a=1,b=3):
    print(a*b)
    return a*b
mult()
"""
"""
# wap to print the length of a list . (list is a parameter)

language = ["python","java","php","dotnet"]

def print_len(list):
    print(len(list))

print_len(language)
"""


"""
#wap to print the elements of a list in a single line,(list is a parameter)

heroes = ["thor","iron man","hulk","superman"]

def print_elements(list):
    for items in list:
        print(items,end = " ")

print_elements(heroes)
"""
"""n = 5
def find_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
find_fact(5)"""


'''
def converter(usd_value):
    """coverting USD to INR"""
    inr_value = usd_value*92
    print(usd_value,"USD =",inr_value,"INR")

converter(92)
    '''

'''def find_evenodd(number):
    """finding even and odd"""
    if number %2 != 0:
        print("odd")
    else:
        print("even")
    
find_evenodd(6)'''




