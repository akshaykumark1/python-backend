# syntax
# when an object is created it calls the __init__ method to initialize the state of the object.
# when an object is about to be destroyed it calls the __del__ method to perform any clean up.
class Master:
    def __init__(self,a):
        self.a=a
        print("hello")

    def main(self):
        print("hellow")
        print(self.a)
# when we create an object using the class, it will call the __init__ method
# when the object is no longer needed it will call the __del__ method
obj1=Master("hello")
obj1.main()        

