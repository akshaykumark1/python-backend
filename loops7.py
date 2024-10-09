# reverse a number
a=int(input("enter the number"))
b=0
while(a>0):
    reminder=a%10
    b=b*10+reminder
    a=a//10
print(b)
# another method
a