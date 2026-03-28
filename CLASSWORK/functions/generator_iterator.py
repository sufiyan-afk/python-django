l = [1,2,34,4,6,7,8]
it = iter(l)
print(next(it))
print("hello")
print("world")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(list(l))

def calc(a):
    for i in range(1,a):
        yield i*i
    k = calc(10)
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))