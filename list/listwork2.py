# input 5 names and display it in reverse 

a=[]
limit=int(input("enter the limit"))
for i in range(limit):
    b=input("enter the name")
    a.append(b)
print("reverse order")
for i in a:
    print(i[::-1])

