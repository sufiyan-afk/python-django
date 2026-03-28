sub = ["python","php","java","node","android"]
k=[]

def length (sub):
    return len(sub)

k = map (length,sub)
print(list(k))

k = map(lambda x:len(x),sub)
print(list(k))

k = filter(lambda k :k.startswith("p") , sub)
print(list(k))

l = [2,5,9,8,25,49,45,81,144,22,23]
l = filter(lambda x : ,l)
print(list(l))

from functools import reduce
l = [1,3,4,5,5,6]

def maximum(a,b):
    if(a>=b):
        return a
    else:
        return b
r = reduce(maximum,l)
print(r)

r = reduce(lambda a,b : a if a>=b else b , l)
print(r)