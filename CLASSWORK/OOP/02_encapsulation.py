# class test:
#     a = 10              # public
#     _b = 20             #protected
#     __c = 30            #private

#     def set(self,a):
#         self.__c = a

#     def get(self):
#         return self.__c
    
#     def test(self):
#         print(self.a,self.b)


# class demo(test):

#     def disp(self):
#         print(self._b)

# t = test()
# t.set(500)
# print(t.get())

# #print(dir(t))

# # print(t.a)
# # print(t._b)
# # print(t._test__c) 

class person:
    __name = "Sufiyan"
    # def private(self,__name):
    #     if __name != 0:
    #         print("none")
    #     else:
    #         print(__name)

    def get_name(self,__name):
        return __name
    
p1 = person()
print(p1.get_name())