#library in python
library=[]

def addbook():
    book_name=input("enter book name: ")
    writer=input("enter the writername: ")
    year=int(input("enter the year: "))
    library.append({
        "name":book_name,
        "writer":writer,
        "year":year

    })
    print("book added successfully")