import json
from abc import ABC, abstractmethod
from datetime import datetime

"""
ABC (Abstract Base Class):
- Is class ka direct object nahi ban sakta
- Sirf inherit karne ke liye use hoti hai
- Ye ek blueprint define karti hai (what must be implemented)
"""

class BankAccount(ABC):

    """
    Constructor:
    - owner → account holder ka naam
    - balance → private (encapsulation)
    - account_number → unique identifier
    - pin → private security field
    """
    def __init__(self, owner, balance, account_number, pin):

        import hashlib

        self.owner = owner
        self.__balance = balance          # private (encapsulation)
        self.account_number = account_number
# check : already hashed hai ya nahi
        if len(str(pin)) == 64:   #SHA256 hash length
            self.__pin = pin 
        else:
            self.__pin = hashlib.sha256(str(pin).encode()).hexdigest()
        self.transaction_history = []     # list of transactions (audit trail)
        self.pin_attempts = 0             # wrong PIN attempts counter

    """
    Abstract Method:
    - Har child class ko is method ko define karna hi padega
    - Polymorphism enable karta hai
    """
    @abstractmethod
    def show_balance(self):
        pass

    """
    Deposit Method:
    - Controlled way to modify balance
    - Direct access allowed nahi (encapsulation)
    - Transaction history maintain karta hai
    """
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append({
                "type": "Deposit",
                "amount": amount,
                "balance": self.__balance
            })
        else:
            print("Invalid deposit amount!")

    """
    Withdraw Method:
    - Validates amount
    - Checks sufficient balance
    - Transaction history maintain karta hai
    """
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        if self.__balance >= amount:
            self.__balance -= amount
            self.transaction_history.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": self.__balance
            })
        else:
            print("Insufficient Balance")

    """
    Getter Method:
    - Private balance ko safely access karne ke liye
    """
    def get_balance(self):
        return self.__balance

    """
    Setter Method:
    - Balance ko controlled way me update karta hai
    """
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

    """
    PIN Verification:
    - Entered PIN ko stored PIN se compare karta hai
    - Security check
    """
    def verify_pin(self, entered_pin):
        import hashlib
        return self.__pin ==  hashlib.sha256(str(entered_pin).encode()).hexdigest() 

    """
    Change PIN:
    - Old PIN verify karta hai
    - New PIN set karta hai
    """
    def change_pin(self, old_pin, new_pin):
        import hashlib
        if self.verify_pin(old_pin):
            self.__pin = hashlib.sha256(str(new_pin).encode()).hexdigest()
            print("PIN changed successfully!")
        else:
            print("Wrong old PIN")

    
    def transfer(self, target_account, amount):
        """
        Fund Transfer Method:
        self = sender account
        terget_account = receiver account
        """
        #1.basic validation
        if amount <= 0:
            print("Invalid amount!")
            return
        
        if self.account_number == target_account.account_number:
            print("Cannot transfer to same account!")
            return
        


        #2. sufficient balance check
        if self.get_balance() < amount:
            print("Insufficient balance for transfer!")
            return
        

        # #3. perform transfer (atomic style)
        old_balance = self.get_balance()
        self.withdraw(amount)

        if self.get_balance() == old_balance:
            return   #withdraw fail
        
        target_account.deposit(amount)


        #4. add transfer record(extra clarity)
        
        self.transaction_history.append({
            "type" : "Transfer Sent",
            "amount": amount,
            "to" : target_account.account_number,
            "balance": self.get_balance(),
            "date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        target_account.transaction_history.append({
            "type":"Transfer recieved",
            "amount":amount,
            "from": self.account_number,
            "balance":target_account.get_balance(),
            "date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Rs.{amount} transferred successfully to {target_account.account_number}")



"""
Inheritance:
- SavingsAccount, BankAccount ko extend karta hai
- Extra feature: interest_rate
"""
class SavingsAccount(BankAccount):

    """
    Constructor:
    - Parent class constructor call (super)
    - Extra attribute: interest_rate
    """
    def __init__(self, owner, balance, account_number, pin, interest_rate):
        super().__init__(owner, balance, account_number, pin)
        self.interest_rate = interest_rate

    """
    Polymorphism:
    - Parent ke abstract method ko override kiya
    """
    def show_balance(self):
        print(f"Owner      : {self.owner}")
        print(f"Account no : {self.account_number}")
        print(f"Balance    : Rs.{self.get_balance()}")
        print(f"Interest   : {self.interest_rate}%")

    """
    Interest Calculation:
    - Balance pe interest calculate karke add karta hai
    - Deposit method reuse kiya (code reuse / DRY principle)
    """
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest added! New balance : {self.get_balance()}")


    def withdraw(self,amount):
        minimum_balance = 1000
        if amount <= 0:
            print("Invalid amount!")
            return
        
        if self.get_balance() - amount < minimum_balance:
            print(f"Minimum balance of Rs.{minimum_balance} must be maintained!")
            return
        super().withdraw(amount)



class CurrentAccount(BankAccount):

    def __init__(self, owner, balance, account_number, pin, overdraft_limit):
        super().__init__(owner, balance, account_number, pin)
        self.overdraft_limit = overdraft_limit

    def show_balance(self):
        print(f"owner      : {self.owner}")
        print(f"Account no : {self.account_number}")
        print(f"Balance    : Rs.{self.get_balance()}")
        print(f"overdraft  : Rs.{self.overdraft_limit}")

    #override withdraw 
    def withdraw(self, amount):
        
        if amount <= 0:
            print("Invalid amount!")
            return
        
        #overdraft allow
        if self.get_balance() + self.overdraft_limit >= amount:
            #balance negative ho sakta hai
            self.set_balance(self.get_balance() - amount)

            self.transaction_history.append({
                "type": "Withdrawal",
                "amount" : amount,
                "balance": self.get_balance()
            })

        else:
            print("Overdraft limit exceeded!")



"""
Persistence Layer (File Handling):
- JSON file me data save/load karna
- Program band hone ke baad bhi data safe rahe (persistence)
"""

def save_accounts(accounts):
    data = {}

    # Object → Dictionary conversion (serialization)
    for acc_no, acc in accounts.items():
        acc_data = {
            "owner": acc.owner,
            "balance": acc.get_balance(),
            "pin": acc._BankAccount__pin,   # private access (educational purpose)
            "type": acc.__class__.__name__
        }

        #extra fields based on type
        if isinstance(acc , SavingsAccount):
            acc_data["interest"] = acc.interest_rate

        elif isinstance(acc, CurrentAccount):
            acc_data["overdraft"] = acc.overdraft_limit

        data[acc_no] = acc_data

    # File me write
    with open("accounts.json", "w") as f:
        json.dump(data, f,indent = 4)


def load_accounts():
        
    try:
        # File read
        with open("accounts.json", "r") as f:
            data = json.load(f)

        accounts = {}

        # Dictionary → Object conversion (deserialization)
        for acc_no, acc in data.items():
            if acc.get("type") == "SavingsAccount":
                accounts[acc_no] = SavingsAccount(
                    acc["owner"],
                    acc["balance"],
                    acc_no,
                    acc["pin"],
                    acc.get("interest",0)
                )
            elif acc.get("type") == "CurrentAccount":
                accounts[acc_no] = CurrentAccount(
                    acc["owner"],
                    acc["balance"],
                    acc_no,
                    acc["pin"],
                    acc.get("overdraft",0)
                )
                
        return accounts

    except FileNotFoundError:
        # Agar file exist nahi karti
        return {}


# ====================================================
#                ATM SYSTEM (Main Program)
# ====================================================

print("\n===== ATM SYSTEM =====")

"""
Load accounts from file:
- Agar file me data hai → use karo
- Nahi hai → default accounts create karo
"""
accounts = load_accounts()

if not accounts:
    accounts = {
        "ACC001": SavingsAccount("sufiyan", 5000, "ACC001", 1234, 10),
        "ACC002": SavingsAccount("Mohammed", 8000, "ACC002", 4321, 8),
    }

# Step 1: Account validation
acc_input = input("Enter Account number: ")
account = accounts.get(acc_input)

if account and acc_input == account.account_number:

    """
    Security Note:
    - PIN plain form me store ho raha hai (educational purpose)
    - Real system me hashing use hota hai
    """

    # Step 2: PIN verification (max 3 attempts)
    while account.pin_attempts < 3:
        try:
            pin_input = int(input("Enter PIN: "))
        except ValueError:
            print("PIN must be numeric!")
            continue

        if account.verify_pin(pin_input):
            account.pin_attempts = 0
            print(f"\nWelcome, {account.owner}!")

            # Step 3: ATM Menu loop
            while True:
                print("\n--- ATM Menu ---")
                print("1. Show Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Add Interest")
                print("5. Transaction History")
                print("6. Change PIN")
                print("7. Transfer Money")
                print("8. Create New Account")
                print("9. Exit")

                choice = input("Enter choice: ")

                if choice == "1":
                    account.show_balance()

                elif choice == "2":
                    try:
                        amount = int(input("Enter deposit amount: "))
                    except ValueError:
                        print("Invalid input!")
                        continue
                    account.deposit(amount)

                elif choice == "3":
                    try:
                        amount = int(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    except ValueError:
                        print("Invalid input!")

                elif choice == "4":
                    account.add_interest()

                elif choice == "5":
                    if not account.transaction_history:
                        print("No transactions yet.")
                    else:
                        for t in account.transaction_history:
                            print(f"{t['type']} | Rs.{t['amount']} | Balance: Rs.{t['balance']}")

                elif choice == "6":
                    try:
                        old = int(input("Enter old PIN: "))
                        new = int(input("Enter new PIN: "))
                        account.change_pin(old, new)
                    except ValueError:
                        print("PIN must be numeric!")

                elif choice == "7":
                    target_acc_no = input("Enter target account number: ")
                    target_account = accounts.get(target_acc_no)

                    if not target_account:
                        print("Target account not found!")
                        continue

                    try:
                        amount = int(input("Enter amount: "))
                    except ValueError:
                        print("Invalid input!")
                        continue
                    account.transfer(target_account,amount)


                elif choice == "8":
                    # Account type input
                    print("\nSelect Account type:")
                    print("1.Savings Account")
                    print("2. Current Account")

                    acc_type = input("enter choice: ")
                    
                    name = input("Enter your name: ")

                    try:
                        pin = int(input("set 4 digit PIN: "))
                        if len(str(pin)) != 4:
                            print("PIN must be 4 digits!")
                            continue
                    except ValueError:
                        print("invalid input!")
                        continue

                    #ACCOUNT number generate (common)
                    new_acc_no = f"ACC{len(accounts) + 1:03}"
                    
                    #SavingsAccount
                    if acc_type == "1":
                        try:
                            balance = int(input("Enter Initial deposit: "))
                            if balance < 0:
                                print("Invalid amount!")
                                continue
                        except ValueError:
                            print("Invalid input!")
                            continue
                    
                        new_account = SavingsAccount(name,balance , new_acc_no , pin , 5)


                    # current Account
                    elif acc_type == "2":

                        try:
                            overdraft = int(input("Enter overdraft limit : "))
                            if overdraft < 0:
                                print("Invalid overdraft!")
                                continue
                        except ValueError:
                            print("Invalid input!")
                            continue
                        
                        balance = 0     

                        new_account = CurrentAccount(name , balance , new_acc_no , pin , overdraft)
                        
                    else:
                        print("Invalid account type!")
                        continue

                    #store + save
                    accounts[new_acc_no] = new_account

                    print(f"\n Account Created successfully!")
                    print(f"Account number: {new_acc_no}")

                    save_accounts(accounts)


                elif choice == "9":
                    print("\nSession Summary:")
                    print(f"Final Balance: Rs.{account.get_balance()}")

                    # Save data before exit
                    save_accounts(accounts)

                    print("Thank you! Goodbye.")
                    break

                else:
                    print("Invalid choice!")

            break

        else:
            account.pin_attempts += 1
            if account.pin_attempts == 3:
                print("Account locked!")
            else:
                print(f"Wrong PIN! {3 - account.pin_attempts} attempts left.")

else:
    print("Account not found!")