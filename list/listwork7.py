# remove the duplicate from list
l=[100,200,300,100,200,400,500,100,200]
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)

