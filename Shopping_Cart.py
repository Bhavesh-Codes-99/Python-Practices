import os 

# The place for Global Variables
Cart = []

# For Adding new Item in the cart
def AddItems():
    os.system("cls")
    Item = input("What is the Item that you want to enter ?")
    Item_price = float(input("Enter the price of that Element :-"))
    PriceTagedItem = (Item.lower(), Item_price)
    Cart.append(PriceTagedItem)

# For Deleting the Items in Cart   
def RemoveItems():
    os.system("cls")
    Item = input("Which item do you want to remove ??")
    for i in Cart:
        if(i[0]==Item.lower()):
            Cart.remove(i)
            print(Item," was removed Successfully from the cart.")
            break
    else:
        print("No such Item was Found.")

# For viewing the list of Items in the Cart
def ViewCart():
    os.system("cls")
    print("Here is the list of Items present in your cart :- ")
    for item in Cart:
        print(item[0],"   -/",item[1])

# For Calculating the Total Cost of the Cart
def Total():
    os.system("cls")
    Sum = 0
    print("These are the items sent for Billing :- ")
    for item in Cart:
        print(item[0],"   -/",item[1])
        Sum += item[1]

    print("\n So the total bill of the Cart becomes :-",Sum)

#For Searching the items in Cart
def SearchItem():
    os.system("cls")
    Item = input("Enter the item to be searched for :-")
    for item in Cart:
        if(item[0]==Item.lower()):
            print("Yes the item exists in the Cart.")
            break
    else:
        print("No the item doesn't Eixists in your Cart \nWould you like to add to the cart ??")

# For Emptying the Cart
def EmptyCart():
    os.system("cls")
    Cart.clear()


# The main Program starts from here ...
print("-- Hello and welcome to Bhavesh's Store --\n Take a cart with you and let's get Ready for the Shopping !!")

while(True):

    # Instructions for the Users
    choice = int(input("\n\n Enter 1 to add the items in Cart.\n Enter 2 to Remove the items from the cart.\n Enter 3 to View the cart.\n Enter 4 to Calculate the toatl bill of Your cart.\n Enter 5 to search for an item in the Cart.\n Enter 6 to Empty the Cart.\n Enter 7 to Exit the Store."))

    # The match case for selecting the Operation to be performed.
    match choice:
        case 1: 
            AddItems()
        case 2:
            RemoveItems()
        case 3:
            ViewCart()
        case 4:
            Total()
        case 5:
            SearchItem()
        case 6:
            EmptyCart()
        case 7:
            break
        case _:
            print("Entered an Invalid Character.")

print("Thank You!! Visit Again....")