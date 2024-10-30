# input 2 numbers print in between them
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if(a<b):
    while(a<=b):
        print(a,end=" ")
        a+=1
else:
    while a>=b:
            print(a)
            a-=1