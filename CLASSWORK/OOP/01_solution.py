
class car:

    total_car = 0

    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fullname(self):
        return f"i have a car whose brand name is {self.__brand} and model is {self.model} "

    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_desciption():
        return "cars are means of transport"
    
class ElectricCar(car):
    def __init__(self, brand, model , battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"
    



my_tesla = ElectricCar("Tesla" , "model S" ,"85KWH")
# print(my_tesla.battery_size)
# print(my_tesla.fullname())

print(my_tesla.get_brand())
print(my_tesla.fuel_type())


safari  =  car("TATA" , "Safari")
print(safari.fuel_type())

luxury = ElectricCar("TATA" , "batman" ,"90kWH")

print(car.total_car)
# c1 = car(brand="BMW",model="m5")

# print(c1.brand , c1.model)
# print(c1.fullname())


print(my_tesla.general_desciption())   