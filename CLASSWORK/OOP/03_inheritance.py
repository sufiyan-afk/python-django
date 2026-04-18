class A:
    def __init__(self):
        print("A constructor")

    def display(self):
        print("class A display")

class B:

    def __init__(self):
        print("B constructor")

    def display(self):
        print("class B display calling")

class c(A,B):

    def __init__(self):
        B.__init__(self)

    def display(self):
        # return super().display()
        print("C display calling")
        B().display()

c = c()
c.display()