"""
================================================================================
 ATM BANKING SYSTEM
 Author      : Sufiyan
 Description : A console-based ATM system demonstrating core OOP principles
               including Abstraction, Encapsulation, Inheritance, Polymorphism,
               along with file persistence via JSON serialization.
 Tech Stack  : Python 3, ABC module, hashlib (SHA-256), json, datetime
================================================================================
"""

import json
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime


# ================================================================================
#  ABSTRACT BASE CLASS — BankAccount
# ================================================================================
# Purpose   : Defines the common interface and shared behaviour for all account types.
#             Cannot be instantiated directly — acts as a blueprint (Abstraction).
# OOP Concepts:
#   - Abstraction     : Forces subclasses to implement show_balance()
#   - Encapsulation   : __balance and __pin are private; accessed via getters/setters
#   - Inheritance     : Extended by SavingsAccount and CurrentAccount
# ================================================================================

class BankAccount(ABC):

    # ----------------------------------------------------------------------------
    #  Constructor
    #  Initialises account details. PIN is hashed using SHA-256 before storage
    #  to prevent plain-text credential exposure (basic security best practice).
    # ----------------------------------------------------------------------------
    def __init__(self, owner: str, balance: float, account_number: str, pin):
        self.owner = owner
        self.__balance = balance                    # private — enforces encapsulation
        self.account_number = account_number
        self.transaction_history = []               # audit trail for all transactions
        self.pin_attempts = 0                       # tracks consecutive failed PIN entries

        # Accept pre-hashed PIN (e.g., loaded from file) or raw PIN
        # SHA-256 produces a 64-character hex digest
        if len(str(pin)) == 64:
            self.__pin = pin
        else:
            self.__pin = hashlib.sha256(str(pin).encode()).hexdigest()

    # ----------------------------------------------------------------------------
    #  Abstract Method — show_balance()
    #  Each account type displays different fields (e.g., interest rate, overdraft),
    #  so the implementation is deliberately left to subclasses (Polymorphism).
    # ----------------------------------------------------------------------------
    @abstractmethod
    def show_balance(self):
        pass

    # ----------------------------------------------------------------------------
    #  deposit()
    #  Adds funds to the account after validating the amount.
    #  Appends a transaction record for audit purposes.
    # ----------------------------------------------------------------------------
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Invalid deposit amount! Must be greater than zero.")
            return

        self.__balance += amount
        self._log_transaction("Deposit", amount)

    # ----------------------------------------------------------------------------
    #  withdraw()
    #  Base withdrawal logic — validates amount and balance.
    #  Overridden by subclasses to enforce account-specific rules
    #  (e.g., minimum balance for Savings, overdraft for Current).
    # ----------------------------------------------------------------------------
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Invalid amount! Must be greater than zero.")
            return False

        if self.__balance < amount:
            print("Insufficient balance!")
            return False

        self.__balance -= amount
        self._log_transaction("Withdrawal", amount)
        return True

    # ----------------------------------------------------------------------------
    #  get_balance() / set_balance()
    #  Getter and setter for the private __balance field.
    #  Prevents direct external access, maintaining encapsulation.
    # ----------------------------------------------------------------------------
    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, amount: float) -> None:
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount! Balance cannot be negative.")

    # ----------------------------------------------------------------------------
    #  verify_pin()
    #  Hashes the entered PIN and compares it with the stored hash.
    #  Constant-time-like comparison via string equality on hex digests.
    # ----------------------------------------------------------------------------
    def verify_pin(self, entered_pin) -> bool:
        hashed = hashlib.sha256(str(entered_pin).encode()).hexdigest()
        return self.__pin == hashed

    # ----------------------------------------------------------------------------
    #  change_pin()
    #  Validates the old PIN before updating to a new hashed PIN.
    #  Follows the principle of "verify before modify".
    # ----------------------------------------------------------------------------
    def change_pin(self, old_pin, new_pin) -> None:
        if self.verify_pin(old_pin):
            self.__pin = hashlib.sha256(str(new_pin).encode()).hexdigest()
            print("PIN changed successfully!")
        else:
            print("Incorrect old PIN. PIN not changed.")

    # ----------------------------------------------------------------------------
    #  transfer()
    #  Moves funds from this account to a target account.
    #  Uses an atomic-style approach: deducts from sender only if withdrawal
    #  succeeds, then credits the receiver — avoiding partial transfer bugs.
    # ----------------------------------------------------------------------------
    def transfer(self, target_account, amount: float) -> None:
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return

        if self.account_number == target_account.account_number:
            print("Cannot transfer to the same account.")
            return

        if self.get_balance() < amount:
            print("Insufficient balance for transfer.")
            return

        # Atomic-style: capture balance before withdrawal
        balance_before = self.get_balance()
        self.withdraw(amount)

        # Abort if withdrawal did not succeed (e.g., subclass rule blocked it)
        if self.get_balance() == balance_before:
            return

        target_account.deposit(amount)

        # Append transfer-specific records (richer than standard deposit/withdrawal logs)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.transaction_history.append({
            "type"    : "Transfer Sent",
            "amount"  : amount,
            "to"      : target_account.account_number,
            "balance" : self.get_balance(),
            "date"    : timestamp
        })

        target_account.transaction_history.append({
            "type"    : "Transfer Received",
            "amount"  : amount,
            "from"    : self.account_number,
            "balance" : target_account.get_balance(),
            "date"    : timestamp
        })

        print(f"Rs.{amount:.2f} transferred successfully to account {target_account.account_number}.")

    # ----------------------------------------------------------------------------
    #  _log_transaction()  [Protected Helper]
    #  Centralised transaction logger — avoids code duplication across methods.
    #  Prefixed with _ to indicate internal/protected use within the class hierarchy.
    # ----------------------------------------------------------------------------
    def _log_transaction(self, txn_type: str, amount: float) -> None:
        self.transaction_history.append({
            "type"    : txn_type,
            "amount"  : amount,
            "balance" : self.get_balance(),
            "date"    : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


# ================================================================================
#  SAVINGS ACCOUNT
# ================================================================================
# Extends BankAccount with:
#   - Interest rate (credited via add_interest)
#   - Minimum balance constraint on withdrawal (Rs. 1000)
# ================================================================================

class SavingsAccount(BankAccount):

    def __init__(self, owner: str, balance: float, account_number: str, pin, interest_rate: float):
        super().__init__(owner, balance, account_number, pin)
        self.interest_rate = interest_rate          # annual interest rate in percentage

    # Polymorphism — overrides abstract method with Savings-specific display
    def show_balance(self) -> None:
        print(f"\n{'='*35}")
        print(f"  Account Type : Savings Account")
        print(f"  Owner        : {self.owner}")
        print(f"  Account No   : {self.account_number}")
        print(f"  Balance      : Rs.{self.get_balance():.2f}")
        print(f"  Interest Rate: {self.interest_rate}% p.a.")
        print(f"{'='*35}")

    # ----------------------------------------------------------------------------
    #  add_interest()
    #  Calculates interest on the current balance and credits it via deposit().
    #  Reuses deposit() to automatically log the transaction (DRY principle).
    # ----------------------------------------------------------------------------
    def add_interest(self) -> None:
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of Rs.{interest:.2f} credited. New Balance: Rs.{self.get_balance():.2f}")

    # ----------------------------------------------------------------------------
    #  withdraw() — Overridden
    #  Enforces a minimum balance of Rs. 1000 after withdrawal.
    #  Delegates to parent withdraw() if the rule is satisfied.
    # ----------------------------------------------------------------------------
    def withdraw(self, amount: float) -> bool:
        MINIMUM_BALANCE = 1000

        if amount <= 0:
            print("Invalid amount!")
            return False

        if self.get_balance() - amount < MINIMUM_BALANCE:
            print(f"Withdrawal denied! Minimum balance of Rs.{MINIMUM_BALANCE} must be maintained.")
            return False

        return super().withdraw(amount)


# ================================================================================
#  CURRENT ACCOUNT
# ================================================================================
# Extends BankAccount with:
#   - Overdraft facility (allows balance to go negative up to a set limit)
# ================================================================================

class CurrentAccount(BankAccount):

    def __init__(self, owner: str, balance: float, account_number: str, pin, overdraft_limit: float):
        super().__init__(owner, balance, account_number, pin)
        self.overdraft_limit = overdraft_limit      # maximum credit allowed beyond zero balance

    # Polymorphism — overrides abstract method with Current-specific display
    def show_balance(self) -> None:
        print(f"\n{'='*35}")
        print(f"  Account Type : Current Account")
        print(f"  Owner        : {self.owner}")
        print(f"  Account No   : {self.account_number}")
        print(f"  Balance      : Rs.{self.get_balance():.2f}")
        print(f"  Overdraft    : Rs.{self.overdraft_limit:.2f} available")
        print(f"{'='*35}")

    # ----------------------------------------------------------------------------
    #  withdraw() — Overridden
    #  Allows withdrawal beyond zero balance up to the overdraft_limit.
    #  Directly updates balance using set_balance() for overdraft scenarios
    #  since the parent's withdraw() blocks negative balances.
    # ----------------------------------------------------------------------------
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Invalid amount!")
            return False

        effective_balance = self.get_balance() + self.overdraft_limit

        if effective_balance < amount:
            print(f"Withdrawal denied! Overdraft limit of Rs.{self.overdraft_limit} exceeded.")
            return False

        self.set_balance(self.get_balance() - amount)
        self._log_transaction("Withdrawal", amount)
        return True


# ================================================================================
#  PERSISTENCE LAYER — JSON File Handling
# ================================================================================
# Serializes account objects to JSON and deserializes them back.
# Ensures data survives program restarts (persistence).
# ================================================================================

def save_accounts(accounts: dict) -> None:
    """
    Serializes all account objects into a dictionary and writes to 'accounts.json'.
    Stores the hashed PIN directly to avoid re-hashing on reload.
    """
    data = {}

    for acc_no, acc in accounts.items():
        acc_data = {
            "owner"  : acc.owner,
            "balance": acc.get_balance(),
            "pin"    : acc._BankAccount__pin,       # name-mangled private attr (intentional)
            "type"   : acc.__class__.__name__
        }

        if isinstance(acc, SavingsAccount):
            acc_data["interest"] = acc.interest_rate

        elif isinstance(acc, CurrentAccount):
            acc_data["overdraft"] = acc.overdraft_limit

        data[acc_no] = acc_data

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved successfully.")


def load_accounts() -> dict:
    """
    Reads 'accounts.json' and reconstructs account objects.
    Returns an empty dict if the file does not exist (first-run scenario).
    """
    try:
        with open("accounts.json", "r") as f:
            data = json.load(f)

        accounts = {}

        for acc_no, acc in data.items():
            acc_type = acc.get("type")

            if acc_type == "SavingsAccount":
                accounts[acc_no] = SavingsAccount(
                    acc["owner"],
                    acc["balance"],
                    acc_no,
                    acc["pin"],                     # pre-hashed PIN passed directly
                    acc.get("interest", 0)
                )

            elif acc_type == "CurrentAccount":
                accounts[acc_no] = CurrentAccount(
                    acc["owner"],
                    acc["balance"],
                    acc_no,
                    acc["pin"],
                    acc.get("overdraft", 0)
                )

        print(f"{len(accounts)} account(s) loaded from file.")
        return accounts

    except FileNotFoundError:
        print("No existing data found. Starting fresh.")
        return {}


# ================================================================================
#  HELPER — Print Transaction History
# ================================================================================

def print_transaction_history(account: BankAccount) -> None:
    """
    Displays all transactions for the given account in a formatted table.
    Handles accounts with no transaction history gracefully.
    """
    if not account.transaction_history:
        print("No transactions recorded yet.")
        return

    print(f"\n{'─'*60}")
    print(f"  Transaction History — {account.account_number}")
    print(f"{'─'*60}")
    print(f"  {'Type':<20} {'Amount':>10}  {'Balance':>12}  Date")
    print(f"{'─'*60}")

    for txn in account.transaction_history:
        date  = txn.get("date", "N/A")
        ttype = txn.get("type", "")
        amt   = txn.get("amount", 0)
        bal   = txn.get("balance", 0)
        print(f"  {ttype:<20} Rs.{amt:>8.2f}  Rs.{bal:>10.2f}  {date}")

    print(f"{'─'*60}")


# ================================================================================
#  MAIN PROGRAM — ATM Interface
# ================================================================================

def main():
    print("\n" + "="*40)
    print("       WELCOME TO ATM SYSTEM")
    print("="*40)

    # Load persisted accounts; fall back to default demo accounts on first run
    accounts = load_accounts()

    if not accounts:
        accounts = {
            "ACC001": SavingsAccount("Sufiyan",  5000, "ACC001", 1234, 10),
            "ACC002": SavingsAccount("Mohammed", 8000, "ACC002", 4321, 8),
        }

    # ── STEP 1: Account Lookup ────────────────────────────────────────────────
    acc_input = input("\nEnter Account Number: ").strip().upper()
    account   = accounts.get(acc_input)

    if not account:
        print("Account not found. Please check the account number.")
        return

    # ── STEP 2: PIN Verification (max 3 attempts) ─────────────────────────────
    MAX_ATTEMPTS = 3

    while account.pin_attempts < MAX_ATTEMPTS:
        try:
            pin_input = int(input("Enter PIN: "))
        except ValueError:
            print("PIN must be numeric. Try again.")
            continue

        if account.verify_pin(pin_input):
            account.pin_attempts = 0
            print(f"\nWelcome, {account.owner}! Login successful.")
            break
        else:
            account.pin_attempts += 1
            remaining = MAX_ATTEMPTS - account.pin_attempts

            if account.pin_attempts >= MAX_ATTEMPTS:
                print("Account locked due to too many incorrect PIN attempts.")
                return
            else:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
    else:
        return

    # ── STEP 3: ATM Menu ─────────────────────────────────────────────────────
    while True:
        print("\n" + "─"*30)
        print("         ATM MENU")
        print("─"*30)
        print("  1. Show Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Add Interest        [Savings]")
        print("  5. Transaction History")
        print("  6. Change PIN")
        print("  7. Transfer Money")
        print("  8. Create New Account")
        print("  9. Exit")
        print("─"*30)

        choice = input("Select option: ").strip()

        # ── 1. Show Balance ──────────────────────────────────────────────────
        if choice == "1":
            account.show_balance()

        # ── 2. Deposit ───────────────────────────────────────────────────────
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: Rs."))
                account.deposit(amount)
                print(f"Deposited Rs.{amount:.2f}. New Balance: Rs.{account.get_balance():.2f}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        # ── 3. Withdraw ──────────────────────────────────────────────────────
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: Rs."))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        # ── 4. Add Interest (Savings only) ───────────────────────────────────
        elif choice == "4":
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest is only applicable to Savings Accounts.")

        # ── 5. Transaction History ───────────────────────────────────────────
        elif choice == "5":
            print_transaction_history(account)

        # ── 6. Change PIN ────────────────────────────────────────────────────
        elif choice == "6":
            try:
                old = int(input("Enter current PIN: "))
                new = int(input("Enter new PIN: "))
                account.change_pin(old, new)
            except ValueError:
                print("PIN must be numeric.")

        # ── 7. Transfer Money ────────────────────────────────────────────────
        elif choice == "7":
            target_acc_no = input("Enter target account number: ").strip().upper()
            target        = accounts.get(target_acc_no)

            if not target:
                print("Target account not found.")
                continue

            try:
                amount = float(input("Enter transfer amount: Rs."))
                account.transfer(target, amount)
                save_accounts(accounts)
            except ValueError:
                print("Invalid input!")

        # ── 8. Create New Account ────────────────────────────────────────────
        elif choice == "8":
            print("\n  Select Account Type:")
            print("  1. Savings Account")
            print("  2. Current Account")

            acc_type = input("  Choice: ").strip()
            name     = input("  Account Holder Name: ").strip()

            try:
                pin = int(input("  Set 4-digit PIN: "))
                if len(str(pin)) != 4:
                    print("  PIN must be exactly 4 digits.")
                    continue
            except ValueError:
                print("  Invalid PIN.")
                continue

            new_acc_no = f"ACC{len(accounts) + 1:03}"

            if acc_type == "1":
                try:
                    balance = float(input("  Initial deposit amount: Rs."))
                    if balance < 0:
                        print("  Invalid amount.")
                        continue
                except ValueError:
                    print("  Invalid input.")
                    continue

                new_account = SavingsAccount(name, balance, new_acc_no, pin, interest_rate=5)

            elif acc_type == "2":
                try:
                    overdraft = float(input("  Overdraft limit: Rs."))
                    if overdraft < 0:
                        print("  Invalid overdraft limit.")
                        continue
                except ValueError:
                    print("  Invalid input.")
                    continue

                new_account = CurrentAccount(name, 0, new_acc_no, pin, overdraft)

            else:
                print("  Invalid account type.")
                continue

            accounts[new_acc_no] = new_account
            save_accounts(accounts)

            print(f"\n  Account created successfully!")
            print(f"  Account Number : {new_acc_no}")
            print(f"  Account Type   : {new_account.__class__.__name__}")

        # ── 9. Exit ──────────────────────────────────────────────────────────
        elif choice == "9":
            print("\n  Session Summary")
            print(f"  Account  : {account.account_number}")
            print(f"  Owner    : {account.owner}")
            print(f"  Balance  : Rs.{account.get_balance():.2f}")

            save_accounts(accounts)
            print("\nThank you for using ATM System. Goodbye!")
            break

        else:
            print("Invalid option. Please select from the menu.")


# ================================================================================
#  Entry Point
# ================================================================================
if __name__ == "__main__":
    main()
