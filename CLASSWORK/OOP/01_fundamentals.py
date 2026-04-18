"""              OOP ( object oriented programming)

1] class = class is a blueprint for creating objects

2] object = Object ek class ka instance hota hai.
            Jab class ka blueprint use karke real memory mein ek item create hota hai,
             use object kehte hain. 

3] __init__ function :

constructor - is a special method which is invoked automatically
              when the object is created.

self -- refrence of an object 
              
attributes - Attribute wo variable hota hai jo kisi 
            class ya object ke saath associated hota hai. 
            Ye object ka data/state store karta hai.

            types of attributes
            1. class.attr
            2.obj.attr

Self - self ek parameter hota hai jo current object ko refer karta hai.
 Iske through object apne khud ke attributes aur methods access kar sakta hai.
   Ye hamesha method ka pehla parameter hota hai

   methods -- methods are functions that belong to object

 static method--  Static method wo method hota hai jo class ke andar define hota hai 
   lekin kisi specific object se related nahi hota.
 Isme self parameter nahi hota aur ise bina object banaye directly class se call kar sakte hain.
   @staticmethod decorator use hota hai.  

   static method defn -- methods that dont use the self parameter (work at class level)

   encapsulation -- wrapping up of data members and member functions in a single unit i.e class


    inheritance - inheritance in python is an object in which base class give its properties to dericed class
        
        types of inheritance :
        1.single inheritance -- parent to child
        2. multiple inheritance -- one parent two child
        3. multiple  inheritance -- parent to child to grandchild
        4. hybrid inheritance -- combination of all of this
"""


class student: #class

    @staticmethod   # static method 
    def institute():
        print("Tops Technologies")
        print("\n.")
    print("Adding new student in database")

    def __init__(self):         # default constructors
        print("STUDENT DETAILS")


# parameterised constructor
    def __init__(self,fullname,course,age):    #constructor or __init__ function
        self.name = fullname
        self.course = course
        self.age = age


s1 = student("Sufiyan Asif Tal","Python full stack",24)   #object
s1.institute()

print(s1.name)
print(s1.course)
print(s1.age)

print("\n")
s2 = student("Kaif Khan","Python full stack",23)
print(s2.name)
print(s2.course)
print(s2.age)

