# lambda function

number = [11 , 20 , 31 , 40 , 51 ,60 , 71 , 80 , 91 , 100]

def even(x):
    return x % 2 == 0

evens = list(filter(even , number))
print(f"Even numbers : {evens}")