from datetime import date, timedelta #importing date, timedelta from datetime 
list1=[] # empty list to add borrower information
def details(price,books,bookId): #defining function and calling variables in parameters
    book = str(input("Which book you want to lend: ")) #ask user the name of books
    if (book in books): #if name of books is contained in Books lists
        idNo=int(input("Enter book id number: ")) #ask user id of book      
        if (idNo in bookId): #if id number is contained in bookId list
            list1.append(idNo) #add id number in list1
            list1.append(book) #add book in list1
            borrowerName = str(input("Enter your name: ")) #asking user to enter name
            list1.append(borrowerName) #add user name in list1
            address = str(input("Enter your address: ")) #asking user to enter address           
            phoneNo=int(input("Enter your phone number: ")) #asking user to enter phone number
            rate=price[idNo-1] #assigning rate vriable with price 
            print("The price of lending "+book+" book is $"+str(rate)) #prints price of lending books with rate
            today=date.today() #assiging today with current date
            expireDate=today+timedelta(10) #assigning expire date 10 days after cuttent date
            print("You borrowed book in: ",today)
            print("You should retrun back the book in: ",expireDate)
            print("Thank you for borrowing book. Please return the book in time, otherwise fine will be charged 0.50 cent per day.")
            borrowerNote = open("borrowBookNote.txt","w") #opens files in write mode
            borrowerNote.write("Borrowed book by: "+borrowerName+"\tAddress: "+address+"\tPhone no: "+"\tName of Book: "+book+"\tDate: "+str(today)+"\tPaid: "+str(rate))
            borrowerNote.close() #close file of write mode
        else:
            print("Invalid book id number! Please enter valid id number.")
    else:
        print("Invalid book name! Please enter book correct book name.")
    
            
            
            
            
        
        
    
       
    
    
      
    
    
    
    
    
    

