from multipledispatch import dispatch
class calc:

    @dispatch(int , int ,int)
    def add(self,a,b,c):
        print(f"addition is {a+b+c}")

    @dispatch(int,int)
    def add(self , a , b):
        print(f"addition is {a+b}")

    # def add(self,*a):
    #     sum = 0
    #     for i in a:
    #         sum += i
    #     print(sum)

c = calc()
c.add(100,25,36)
c.add(10,20)



