import datetime
import os
# Datasets
library = []
issued_books = []

# Creating a function in order to add a new book 
def add_book ():
    os.system("cls")
    id = len(library) + 1
    print("  ==== Adding new Book to Library ====\n")
    book = {
        "id" : id,
        "title" : input("Enter the Title of the Book :-"),
        "author" : input("Enter the name of Author :-"), 
        "availability" : True
    }
    library.append(book)
    print("Your book has been added Successfully !!")

    
# Function for Viewing all the books in library
def view_books():
    os.system("cls")
    print("  ==== Books Available in Library ====\n")
    if not library:
        print("No books currently available in Library. \nWant to add some books ?? press 1 in main menu")
        return

    for book in library:
        print("Book Id :- ",book["id"])
        print("Title :- ",book["title"])
        print("Author :- ",book["author"])
        if(book["availability"]):
            print("The Book is AVAILABLE in our Library.")
        else:
            print("The book is currently UNAVAILABLE !!")
        print("\n")

# Function for Searching a book in library
def search_book():
    os.system("cls")
    print("  ==== Searching a book ====\n")
    search = input("Enter the Name(Title) of the Book :- ")
    print("\nFollowing are the results found :-\n")
    found = False
    for book in library:
        if(book["title"].lower() == search.lower()):
            print("Book Id :- ",book["id"])
            print("Title :- ",book["title"])
            print("Author :- ",book["author"])
            if(not book["availability"]):
                print("The book is currently UNAVAILABLE !!")
            found = True
    
    if(found == False):
        print("Book not Found. Try with a book with valid title.")
        

# Function for issuing a book.
def issue_a_book():
    os.system("cls")
    print("  ==== Issuing a book ====\n")
    user = input("What's your name ??")
    book_title = input("Please enter the book that you want to borrow :-")

    found = False
    for book in library:
        if (book_title.lower() == book["title"].lower()):
            if(book["availability"]):
                book["availability"] = False
                issued_books.append({
                  "user":user,
                  "id":book["id"],
                  "title":book["title"],
                  "due_date": datetime.date.today() + datetime.timedelta(days=7)
                })
                found = True
                print("Successfully issued the book \"",book["title"],"\"")
                break
            else:
                print("The book is currently issued to someone.")
                found = True


    if(not found):
        print("The book that you want to borrow was not found.")

# Function for returning the book
def return_book():
    os.system("cls")
    print("  ==== Returning a book ====\n")
    book_title = input("Enter the title of the book :-")
    found = False
    for book in issued_books:
        if (book["title"].lower() == book_title.lower()):
            if(datetime.date.today() > book["due_date"]):
                print("The due date of returning the book is already gone.\n You are late and need to pay the penalty fee.")
                issued_books.remove(book)
                print("Successfully returned the book.")
                found = True            
                break
            else:
                issued_books.remove(book)
                print("Successfully returned the book.")
                found = True
    
    if(found):
        for book in library:
            if(book["title"].lower()==book_title.lower()):
                book["availability"] = True
    else:
        print("The book doesn't belongs to library.")



# The Main Part of the code .

print("\n  ------------ Welcome to Bhavesh's Library Management System --------------")

while(True):
    print("\n\nUser Instruction :-")
    print("Enter 1 to add a book to the Library:-\nEnter 2 to view all the books in the Library:-\nEnter 3 to search a book:-\nEnter 4 to issue a book:-\nEnter 5 to return a book:-\nEnter 6 to Exit the System.")
    choice = int(input("\nEnter your choice :- "))

    match choice:
        case 1:
            add_book()
        case 2:
            view_books()
        case 3:
            search_book()
        case 4:
            issue_a_book()
        case 5:
            return_book()
        case 6:
            break
        case _:
            print("Invalid choice !!")