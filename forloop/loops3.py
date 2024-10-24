# # print 0 to 10 

# for i in range(11):
#     print(i)


# print 10 to 0

# for i in range(10,-1,-1):
#     print(i)

# sum of natural numbers from 1 to n

# a=int(input("enter the number"))
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
#     print(sum)


# sum of even numbers from 1 to n    

# a=int(input("enter the number"))
# sum=0
# for i in range(1,a+1):
#     if(i%2==0):
#         sum=sum+i
#         print(sum)

 #find the sum of two numbers
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# sum=a+b
# print(sum)

# sum of natural,odd,even numbers up to 10
a=10
sum=0
for i in range(1,a+1):
    if(i%2==0):
        sum=sum+i
        print("sum of even numbers",sum)
    else:
        sum=sum+i
        print("sum of odd numbers",sum)
