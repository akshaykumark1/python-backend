# sum of natural
a=int(input("enter the number"))
esum=0
osum=0
nsum=0
for i in range(1,a+1):
    nsum=nsum+i
    if(i%2==0):
        esum=esum+i
    elif(i%2==1): 
        osum=osum+i  
print(esum,"even number")
print(osum,"odd number")
print(nsum,"natural numbers")