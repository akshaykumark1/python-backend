
# reverse a string
a=input("enter the string")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
print(b)
