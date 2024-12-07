# library class work

class book():
    def __init__(self,title,author,copies_available):
        self.title=title
        self.author=author
        self.copies_available=copies_available

    def add_copies(self,number):
        self.copies_available+=number
        print("adds copies to th ebook ")
    def borrow_book(self):
        if self.copies_available > 0:
             print("is available",self.copies_available)
        else:
            print("not is available ")     
    def return_book(self):
        self.copies_available+=1
        print("incresed available copies ")


class library():
    def __init__(self):
        self.book=[]

    def addbook(self,book):
        self.book.append(book)
        print("book added",self.)


                






        
    