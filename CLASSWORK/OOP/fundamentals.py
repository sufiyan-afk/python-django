"""              OOP ( object oriented programming)

1] class = class is a blueprint for creating objects

2] object = 

3] __init__ function :

constructor - is a special method which is invoked automatically
              when the object is created.

self -- refrence of an object 
              
attributes - the data or variables which are stored in class or object
             is known as attributes

            types of attributes
            1. class.attr
            2.obj.attr
"""

class student: #class
    college_name = "TOPS TECHNOLOGIES"   #class attributes
    def __init__(self):         # default constructors
        print("STUDENT DETAILS")


# parameterised constructor
    def __init__(self,fullname,course):    #constructor or __init__ function
        self.name = fullname
        self.course = course
        
        print("adding new student in database")


s1 = student("Sufiyan Asif Tal","Python full stack")   #object
print(s1.name,s1.course)
print(student.college_name)

s2 = student("Kaif Khan","Python full stack")
print(s2.name,s2.course)
print(student.college_name)

