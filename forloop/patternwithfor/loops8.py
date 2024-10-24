# patterns 
# ***
# ***
# ***

# this will print 4 rows of 4 columns of asterisks(*) 
# the outer loop will run 4 times and the inner loop will run 4 times for each outer loop iteration
# thus it will print 4 rows of 4 columns of asterisks(*)
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()

# pattern 
# 123
# 123
# 123    
for i in range (1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()
# pattern
# 111
# 222
# 333
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()    


#  print below pattern 1 to 9 like shown below
# 1 2 3
# 4 5 6
# 6 7 8

n=0
for i in range(1,4):
    for j in range(1,4):
        print(n,end=" ")
        n=n+1
    print()


# print this pattern
# *
# **
# ***
# ****
# how it works
# outer loop will run 4 times
# inner loop will run i times
# it will print * i times
# and then it will go to next line
# so it will print 1, 2, 3, 4 stars
# and so on
# so we get the pattern
for i in range(1,5):
    for j in range(1,i+1):
        print("1",end=" ")
    print()

# print this pattern
#   ***
#   **
#   *
# this will print the pattern
#   ***
#   **
#   *
# how it works
# outer loop will run 10 times
# inner loop will run i times
# it will print * i times
# and then it will go to next line
# so it will print 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 stars
# and then it will go to next line
# and then it will print 9, 8, 7, 6, 5, 4, 3, 2, 1 stars
# and then it will go to next line
# and so on
# so we get the pattern
for i in range(10,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
