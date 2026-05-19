import os
# Creating Class for the Banking system
class BankAccount:
    def __init__(self, account_number, holder_name, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = 0

    # Function for depositing the money..
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("You are entering an invalid deposit amount. Please retry.\nTransaction Failed !!")
            return
        self.balance += deposit_amount
        print("The amount of rupees",deposit_amount,"is successfully deposited to your account.\nTransaction Completed !!")

    # Function for withdrawing the money..
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("This is an invalid amount to recieve from the bank account. Please try again.\nTransaction Failed !!")
            return
        if withdraw_amount > self.balance:
            print("No sufficient Balance in your Bank Account. Please try again with a lower amount.\nOr even if you want to view the balance of your bank, Go to main menu.\nTransaction Failed")
            return
        
        self.balance -= withdraw_amount
        print("Successfull withdrawal of rupees",withdraw_amount,"\nTransaction Successfull !!")

    # Function for checking the Balance...
    def check_balance(self):
        print("checking balance... ")
        print(f"{self.holder_name} Currently your balance in the account is :- {self.balance}")


# Some Global datatypes
accounts = {}
acc_number = 1001
# Now the time for making a multiple objects of our class
def create_account():
    os.system("cls")
    global acc_number
    name = input("Enter the name of the Account Holder :- ")
    acc_type = input("Enter what type of Account you want to Create :-")
    accounts[acc_number] = BankAccount(acc_number,name,acc_type)
    print("Successfully Created your account !!")
    print("Your Account Number (Keep it in mind):- ",acc_number)
    acc_number += 1


# The main functions starts here :- 

print("\n   ---- Bhavesh's Bank of INDIA ----")
print("\n Welcome to Bhavesh Bank's new Branch ... :)")
    
while True:    
    print("\n User Instrunctions :-\nEnter 1 to Create a new Account.\nEnter 2 to View the Balance in your Account.\nEnter 3 to Deposit money in your account.\nEnter 4 to Withdraw money from your account.\nEnter 5 to Exit the Bank.")

    try:
        choice = int(input("Enter your Choice :- "))
    except ValueError:
        print("\nInvalid type entered. Please try again.")
        continue

    match choice:
        case 1:
            create_account()
        case 2:
            os.system("cls")
            number = int(input("Enter your Bank Account number :- "))
            if number in accounts:
                accounts[number].check_balance()
            else:
                print("You entered an invalid Account number.\nTry again with different Account number And if you don't have one you can create it from the main menu.")
        case 3:
            os.system("cls")
            number = int(input("Enter your Bank Account number :- "))
            amount = int(input("Enter the amount you want to Deposit in your Account."))
            if number in accounts:
                accounts[number].deposit(amount)
            else:
                print("You entered an invalid Account number.\nTry again with different Account number And if you don't have one you can create it from the main menu.")
        case 4:
            os.system("cls")
            number = int(input("Enter your Bank Account number :- "))
            amount = int(input("Enter the amount you want to Withdraw from your Account."))
            if number in accounts:
                accounts[number].withdraw(amount)
            else:
                print("You entered an invalid Account number.\nTry again with different Account number And if you don't have one you can create it from the main menu.")
        case 5:
            print("Exited the Bank Successfully !!\nThanks for using our Services...")
            break
        case _:
            print("Entered an Invalid Choice. Please try again.")