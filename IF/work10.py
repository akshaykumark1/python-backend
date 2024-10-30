# input 2 number and print the even and odd number in between them
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if(a<b):
    while a<=b:
        if(a%2==0):
            print(a,"is even")
        else:
            print(a,"is odd")
        a=a+1 
else:
    print("invalid")



