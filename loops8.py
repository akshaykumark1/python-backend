# patterns 
# ***
# ***
# ***

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
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# print this pattern
#   ***
#   **
#   *
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()