from datetime import date #imports date from datetime
list2=[] #making list2 for addinig user inforamation
def returning(books,bookId,list1): #defining function and calling variables
    borrower=str(input("Enter your name: "))
    if (borrower in list1):
        book=str(input("Which book you want to return: " ))        
        if (book in list1):            
            idNo=int(input("Please enter correct book id number: "))
            if(idNo in list1):
                list2.append(book)
                list2.append(idNo)
                list2.append(borrower)
                address = str(input("Enter your address: "))
                list2.append(address)
                phoneNo=int(input("Enter your phone number: "))            
                returnDate = date.today()
                print("The return date is: ",returnDate)
                borrowedDays=int(input("Number of days you borrowed books: "))                  
                if borrowedDays <=10: #if book is returned in more than 10 days
                     print("Thank you!")
                else:
                    print("You didn't return book in 10 days. So you have to pay fine 0.50 cent per day.")
                    def fine():
                        late=int(input("How many days late you return the book: "))
                        charge=late*0.50
                        return charge                
                        print("Your fine is: " +str(fine())+"cent")
                returnBookNote = open("returnBookNote.txt","w")
                returnBookNote.write("Returned by: "+ borrower+"\tName of book: "+book+"\tDate:"+str(returnDate)+"Phone no: "+str(phoneNo)+"\tFine: +str(fine(charge))")
                returnBookNote.close()
            else:
                print("Please enter correct id number!")
        else:
            print("Sorry you haven't borowed "+book+".")
    else:
        print("Sorry you haven't borrowed book!")
            

