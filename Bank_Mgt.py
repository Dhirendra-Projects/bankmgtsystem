import random

class BankAccount:
    
    def __init__ (self,account_number,account_holder,balance=0):
        self.account_number= account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"¥{amount} deposited successfully .Current balance: ¥{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw( self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"¥{amount} withdraw successfully.Current balance: ¥{self.balance}")
        else:
            print("Insufficient balance or invalid amount.") 

    def check_balance(self):
        print(f"Account Balance: ¥ {self.balance}")     

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ¥{self.balance}")


class BankMgtSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self,account_holder):
        #Gererate Random account number with prefic dn suffix
        random_number = random.randint(1000,9999) #Generate a random 4-digits number
        account_number = f"PB10{random_number}D0789"
        account = BankAccount(account_number,account_holder)
        self.accounts[account_number] = account
        print(f"Account created successfully.Account Number:{account_number}")
        return account_number
    
    def get_account(sefl,account_number):
        return sefl.accounts.get(account_number , None) 

    def deposit_to_account(self,account_number,amount):
        account =self.get_account(account_number)
        if account:
            account.deposite(amount)
        else:
            print("Account not fount.")
    def withdraw_from_account(self,account_number,amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Amoount not found.") 

    def display_account(self,account_number):
        account = self.get_account(account_number)
        if account:
            account.display()
        else:
            print("Account not found.")

    def check_amount_account(self,account_number):
        account = self.get_account(account_number)
        if account:
            account.check_balance()
        else:
            print("Account not found.")            

# Example usage:
bank = BankMgtSystem()

#Create an account with user input
print(".....Your Welcome in our bank PBI.....")
account_holder = input("Enter the account holder's name: ")
acc_number = bank.create_account(account_holder)
          
#Menu for deposit and withdrawal
while True:
    print("\n PBI Menu:\n1. Open New Account\n2. Deposit\n3 .Withdraw\n4. Display Account Deatail\n5. Check Available Balance\n6. Exit")
    choise = input("Please Enter your choise (1/2/3/4/5/6):")
    
    if choise == "1":

        new_account =input("Do you want to Open a New Account in our Python Bank of India?  (Yes/No): ")
        if new_account == "Yes":
                 print("...Welcome in PBI..")
                 account_holder = input("Please Enter  your Name: ")
                 acc_number = bank.create_account(account_holder)
        else:
            print(" Welcome Again ....Thanks")           


    elif choise == "2":
        amount = float(input(f"Enter the amount to deposit in account {acc_number}: "))
        bank.deposit_to_account(acc_number,amount)
    elif choise == "3":

        amount = float(input(f"Enter the amount to withdraw form account{acc_number}: "))
        bank.withdraw_from_account(acc_number,amount)
    elif choise == "4":
        bank.display_account(acc_number)
    elif choise == "5":
        bank.check_amount_account(acc_number)
    elif choise == "6":
        print( f"Thanks {account_holder} for using our Python Bank Services..... ")
        break
    else:
        print(f"Invalid choise Dear {account_holder} .Please enter a valid option ")        

 