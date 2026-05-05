# # Question1 : create a student class that takes name & marks of 3 subjects as arguments in constructor,
# #            then create a method to print average.

# class student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for value in self.marks:
#             sum += value
#         print(f"hi {self.name} your average of marks is {sum/3}")
        
# s1 = student("Sufiyan",[80,50,70])
# s1.get_avg()


# from abc import ABC , abstractmethod
# class BankAccount(ABC):
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance   #private

#     @abstractmethod
#     def show_balance(self):      #abstract method
#         pass

#     def deposit(self,amount):
#         self.__balance = self.__balance + amount
#         return self.__balance
    
#     def withdraw(self,amount):
#         if self.__balance >= amount:
#             self.__balance = self.__balance - amount
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print(f"current balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("invalid amount!")

# class savings_account(BankAccount):
#     def __init__(self, owner, balance,interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.get_balance() * self.interest_rate / 100
#         self.deposit(interest)
#         print(f"Interest added! New balance : {self.get_balance()}")
        
# acc = BankAccount("Sufiyan",5000)

# sa = savings_account("Sufiyan",5000,10)
# sa.show_balance()
# sa.add_interest()
# sa.show_balance()
"""
class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited from your account")
        print(f"total balance = Rs.{self.get_balance()}")
    
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited on your account")
        print(f"total balance = Rs.{self.get_balance()}")

    def get_balance(self):
        return self.balance

Account1 = Account(10000,"ACC001")   
Account1.debit(1000)
Account1.credit(500) 
"""
# del Account1
# print(Account1)


