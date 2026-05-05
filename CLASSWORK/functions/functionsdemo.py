# # #functions in python
# # def hello():
# #     #your code goes here
# #     print("Hello from function")


# # def greet():
# #     print("Hello welcome to python")
# #     print("this is my first funtion")
# # greet()
# # greet()
# # greet()

# #parameter and argumnets

# def add_number(a,b):
#     result = a + b
#     print(a,'+',b,'=',result)

# add_number(10,20)
# add_number(20,5)
# add_number(30,50)

# return statement

#without return - just print
def add_v1(a,b):
    print(a+b)    #prints but gives nothing

#with return - gives the value back
def add_v2(a,b):
    return a+b   # send the return back by adding the arguments given 

result = add_v2(10,20)
print("the answer is ",result)

total = add_v2(3,4) + add_v1(10,10)
print("grand total",total)