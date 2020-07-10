import borrowBook  #imports borrowBook module
import returnBook  #imports returnBook module 
import read        #imports read moudle
import updateBooks #imorts updateBooks module

bookId=[1,2,3]  #list of book id
books=["Harry Potter","Start With Why","Programming With Python"] #list of avaliable
quantity= [30,10,20] #list of quantity
price=[2,1.5,1.5]  #list of price for borrowing books

ask=str(input("Do you want to enter in library system? \nyes/no:" )) #ask user to whether to enter or not
while ask=="yes": #if user answer is yes start while loop
    read.avaliableBooks() #calls read.avaliableBooks file
    option=int(input("Please press \nkey 1 for borrowing book \nkey 2 for returning book \nkey 3 for exit ")) # again ask user to select option                      
    if option==1: # if user option is 1 
        print("Please fill the form below with correct information:") #Ask user for filling form for borrowing books
        borrowBook.details(price,books,bookId) #calls function
        updateBooks.updateDeduct(quantity,borrowBook.list1[0],0) #calls function to update avaliable books 
        updateBooks.updateAvaliableBook(quantity) #calls function 
    elif option==2: # if user option is 2
        returnBook.returning(books,bookId,borrowBook.list1) #calls function for unpading books
        updateBooks.updateAdd(quantity,returnBook.list2[1],1) #calls functions
        updateBooks.updateAvaliableBook(quantity) #calls functions
    elif option==3: #if user options 3
        print("Thank you for visiting library.") #Print mesasge
        break #End while loop
    else:              
        print("Incorrect key! Please enter correct key.")
while ask=="no": #if user answer is no 
    print("Thank you!")# print message
    break #end while loop
    
    
        
    



    
