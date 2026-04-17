# Question1 : create a student class that takes name & marks of 3 subjects as arguments in constructor,
#            then create a method to print average.

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(f"hi {self.name} your average of marks is {sum/3}")
        
s1 = student("Sufiyan",[80,50,70])
s1.get_avg()