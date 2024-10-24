# program to accept the cost bike and display the road tax to be paid according  to the ceiteria
# cost price(in rs)
# tax >100000 15%
# tax >50000 and <=100000 10%
#<=50000 5%
a=int(input("enter the cost of bike"))
if(a>100000):
    tax=a*0.15
    print("tax to be paid",tax)
elif(a>50000):
    tax=a*0.10
    print("tax to be paid",tax)
else:
    tax=a*0.05
    print("tax to be paid",tax)q
