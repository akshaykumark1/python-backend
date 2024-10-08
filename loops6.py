# find the factorial of a number
a=int(input("enter the number"))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print(factorial)