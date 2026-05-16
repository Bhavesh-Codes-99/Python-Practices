import os
# Basic Databases
monthly_income = []
expenses = []
categories = ("food", "transport", "rent", "entertainment", "shopping", "health")
used_categories = set()

# Function for entering the monthly income
def set_monthly_income():
    os.system("cls")
    amount = float(input("Enter the monthly income value that you want to set :-"))
    source = input("From where do you earn that income ??")

    monthly_income.append({
        "amount":amount,
        "source":source
    })
    print("Your monthly salary is set as,",amount,"From the Source :-",source)


# Function for Adding the Expences
def add_expenses():
    os.system("cls")
    print("Following are the Available categories for the expenses :-")
    for i in categories:
        print(i,',', end = " ")
    category = input("\nSo now choose one of the categories for expeses:- ")
    amount = float(input("Also enter the amount of Expense :- "))
    if( category.lower() in categories ):        
        description = input("Description about the category (For.Eg --> Lunch at restaurant) ")

        expenses.append({
            "amount":amount,
            "category":category.lower(),
            "description":description
        })

        print("Expenses added Successfully !!")

        used_categories.add(category.lower())
    else:
        print("You entered an Invalid Category")


# Function for showcasing the summary.
def show_summary():
    os.system("cls")
    # Calculating the total income
    if(len(monthly_income) == 0):
        print("Income is 0. First enter your income by pressing 1.")
        return
    Sum = 0
    print("Your monthly income :- ")
    for incomes in monthly_income:
        print(incomes["amount"],"rupees from",incomes["source"])
        Sum += incomes["amount"]
    print("So your Total income (monthly) :- ", Sum)

    # Calculating the Expenses 
    TOTAL_expenses = 0
    print("\nYour Category Wise Expences :-")
    for Expense in expenses:
        print(Expense["category"],":-",Expense["description"])
        print("Expencse on",Expense["category"]," --> ",Expense["amount"],"\n")
        TOTAL_expenses += Expense["amount"]

    print("So your Total Expenses this month :-", TOTAL_expenses)

    # Calculating the Savings
    Savings = Sum - TOTAL_expenses
    print("So your total savings of the Month :-", Savings)

    # Calculating the saftey margin
    if(Savings<=0):
        print("Danger !! You have overspent this month. \nYour expenses were more than the income.")
    elif((Savings/Sum)*100 >= 50.0):
        print("Excellent !! Your savings are 50% more than your Monthly income.")
    elif ((Savings/Sum)*100 < 50.0):
        print("Warning !! Your savings are less than 50%.")
    

# Function for calculating the Maximum expense.
def max_expense():
    os.system("cls")
    print(" === Biggest Expense of the Month ===")
    if len(expenses) == 0:
        print("No expenses added yet!")
        return
    Max_Expense = 0
    Max_Expense_Dict = {}
    for i in expenses:
        if(Max_Expense < i["amount"]):
            Max_Expense = i["amount"]
            Max_Expense_Dict = i
    print("Category :-",Max_Expense_Dict["category"])
    print("Description :-",Max_Expense_Dict["description"])
    print("Amount :-",Max_Expense_Dict["amount"])



# The loop of the main function
print("  ----- Bhavesh's Expense Tracker -----")
print("\n Welcome to my Monthly Expense Tracker.\n Hope you enjoy using it ...:)")
while(True):
    print("\nUser Instructions :- \n1. Enter 1 to add your monthly income \n2. Enter 2 to add your mothly expenses \n3. Enter 3 to View the summary of Expeses and Savings \n4. Enter 4 to See where you spent most of your income this month\n5. Enter 5 to Exit the Program.")

    choice = int(input("Enter your choice :-"))

    match choice:
        case 1:
            set_monthly_income()
        case 2:
            add_expenses()
        case 3:
            show_summary()
        case 4:
            max_expense()
        case 5:
            break
        case _:
            print("Enterd an invalid index. Please try again !!")