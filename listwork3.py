# remove the duplicate from list
a=[1,2,3,2,3,5]
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
print(a1)
