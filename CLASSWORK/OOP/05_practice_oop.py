# class GymMember:
#     def __init__(self,name , age , plan):
#         self.name = name
#         self.age = age
#         self.plan = plan
#         self.is_active = True

#     def workout(self,exercise):
#         print(f"{self.name} is doing {exercise}")

#     def __str__(self):
#         return f"member: {self.name} | plane : {self.plan}" 

# class PremiumMember(GymMember):
#     def __init__(self, name, age, plan , trainer):
#         super().__init__(name, age, plan)
#         self.trainer = trainer

#     def personal_trainer(self):
#         print(f"{self.name} is training with {self.trainer}")






# sufiyan = GymMember("sufiyan",24, "monthly")
# nabeel = GymMember ("nabeel",23,"annual")

# sufiyan.workout("push pull legs")
# nabeel.workout("bro split")

# rayyan = PremiumMember("rayyan", 23 , "annual" , "Cbum sir")

# rayyan.workout("powerlift")
# rayyan.personal_trainer()
# print(rayyan)



# class employee:
#     def __init__(self , name , salary , department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def give_raise(self , percent):
#         self.salary = self.salary + (self.salary * percent /100)
#         return self.salary
    
#     def __str__(self):
#         return f"name : {self.name} | department : {self.department} | salary : {self.salary} "
    
# class Manager(employee):

#     def __init__(self, name, salary, department , team_size):
#         super().__init__(name, salary, department)
#         self.team_size = team_size

#     def add_members(self):
#         self.team_size += 1
#         return self.team_size
    
# emp = employee("sufiyan", 20000 , "backend" , )
# print(emp)

# emp.give_raise(10)
# print(emp)


# mgr = Manager("Husein" , 60000 , "engineering" , 6)
# print(mgr)

# mgr.add_members()
# print(mgr.team_size)

# mgr.give_raise(20)
# print(mgr.salary)


class Vehicle:

    def __init__(self , brand , model , speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerator(self , amount):
        self.speed = self.speed + amount   #existing speed me add karne ke liye

    def brake(self , amount):
        self.speed = self.speed - amount
        if self.speed < 0 :
            self.speed = 0
    
    def __str__(self):
        return f"brand : {self.brand} model : {self.model}  |  speed : {self.speed} km/h"
    
    
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, speed , battery):
        super().__init__(brand, model, speed)
        self.battery = battery 
    
    def accelerator(self , amount):
        if self.battery == 0:
            print("Battery is dead! charge karo")
            return                          # speed mat badhao
        self.speed = self.speed + amount    # parent jaisa speed update
        self.battery = self.battery - 10
        if self.battery < 0:
            self.battery = 0                 #battery negative na ho

    def charge(self,amount):
        self.battery = self.battery + amount
        if self.battery > 100 :
            self.battery = 100               # 100 se uper na jaaye

    def __str__(self):
        return f"{self.brand} {self.model}  |  speed : {self.speed} km/h  | Battery: {self.battery}%"
        

vehcl = Vehicle("Mercedes" , "Benz 2020" , 0)
vehcl.accelerator(100)
print(vehcl)   

vehcl.brake(30)
print(vehcl)


evehicle = ElectricVehicle("TATA" , "Nexon EV" , 0 , 100 )
print(evehicle)

evehicle.accelerator(60)
print(evehicle)

evehicle.charge(30)
print(evehicle)


        