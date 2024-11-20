# input 5 names from user 
try:
    f = open("hlo.txt","x")
except:
    f = open("hlo.txt","w")
limit = int(input("enter the limit"))
for i in range (limit):
    Name = input("enter the name")
    f.write(Name)
    f.write("\n")






