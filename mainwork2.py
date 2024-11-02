library=[]
def addbook():
    book_name=input("enter book name: ")
    writer=input("enter the writername: ")     #adding
    year=int(input("enter the year: "))
    library.append({
        "name":book_name,
        "writer":writer,
        "year":year

    })
    print("book added successfully")

def updatebook():
    book_name=input("enter the book name to update")
    for book in library:
        if book["name"]==book_name:
            book["writer"]= input("enter new writer")
            book["yrear"]= int(input("enter the year"))      #updating
            print("book updated succcessfully")
            return
    print("book not found")      


def removebook():
    book_name=input("enter the bookname to remove")
    for book in library:
        if book["bookname"]==book_name:
            library.remove(book)
            print("book removed successfully")  #removing
            return
    print("book not found") 


def view_books():
    if library:
        print("list of all books")
        for book in library:
            print(f"name:{book['name']},writer:{book['writer']},year:{book['year']}")   # view all books
            print()
    else:
        print("no books in library")        
            
def main():
    print("welcome to library")
    while True:
        print("""1.add book
              2.update book
              3.remove book
              4.view book
              5.exit""")         
        choice = input("select any: ")

        if choice == '1':
            addbook()
        elif choice == '2':
            updatebook()
        elif choice == '3':
            removebook()
        elif choice == '4':
            view_books()
        elif choice == '5':
            print("exit the library")              
            break
        else:
            print("invalid")

main()