# a company decides to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.


a=int(input("enter the salary"))
b=int(input("enter the year of service"))
if(b>5):
    print(a*5/100)
else:
    print("no bonus")