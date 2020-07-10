def updateDeduct(quantity,bookId,deductOrAdd): #defining function and calling variables 
    if deductOrAdd == 0:
         quantity[bookId-1] = quantity[bookId-1]-1
def updateAdd(quantity,bookId,deductOrAdd):
    if deductOrAdd==1:
        quantity[bookId-1] = quantity[bookId-1]+1
def updateAvaliableBook(quantity): #defining function and quantity paramater
    file = open("avaliableBooks.txt","w") # opens files for writing 
    file.write(">>>>>>WELCOME TO IIC Library>>>>>>\n"+

" Book id.  Name of books            Author             Quantity    Rate\n"+ 
"  1.       Harry Potter             JK Rowling         "+str(quantity[0])+"          $2"+ "\n"+
"\n"+                                           
"  2.       Start With Why           Simon Sinek        "+str(quantity[1])+"          $1.5"+"\n"+
"\n"+
"  3.       Programming With Python  John Smith         "+str(quantity[2])+"          $1.5"+"\n"+         
"\n")                                     
    file.close()

