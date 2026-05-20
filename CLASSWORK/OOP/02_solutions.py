
class Account:

    def __init__(self , account_holder_name , balance):
        self.account_holder_name = account_holder_name
        self.__balance = balance

    def show_balance(self ):
        print (f"{self.account_holder_name}  has a balance : {self.__balance}")

user1 = Account ("Sufiyan" , 20000)
user1.show_balance()

user2 = Account("Suhi"  , 200000)
user2.show_balance()