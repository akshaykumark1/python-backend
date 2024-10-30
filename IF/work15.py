# calculate the electricity bill (accept number of unit from user) according to the following criteria 
#first 100 unit no charge,next 100 unit 5 rupee per unit, next 200 unit 10 rupee per unit,


a=int(input("enter the unit"))
if(a<100):
    print("no charge")
elif (a<=200):
    a=a-100
    cost=a*5
elif(a>200):
    a=a-200
    cost=(a*10)+500
else:
    print("invalid")
        
