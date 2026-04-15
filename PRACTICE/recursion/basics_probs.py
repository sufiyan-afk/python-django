"""
#recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)"""

# def fact(n):
#    if(n==1 or n == 0):
#       return 1
#    return fact(n-1) * n

# print(fact(5))

def calc_sum(n):
    for i in range(n):
        sum = sum+1
        return sum
calc_sum(5)