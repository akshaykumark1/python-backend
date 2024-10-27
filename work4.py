# nested if
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b):
    if(a>c):
        print(a," is greater")
    else:
        print(c,"is greater")
else:
    if(b>c):
        print(b," is greater")
    else:
        print(c,"is greater")


        
# another way with out nested if
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b and a>c):
    print(a,"is greater")
elif(b>c):
    print(b,"is greater")
else:
    print(c,"is greater")


