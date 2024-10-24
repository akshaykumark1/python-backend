# # # print pattern like this 
# # # 1 2 3
# # # 2 3 4
# # # 3 4 5
# for i in range(1,4):
#     for j in range(i,i+3):
#         print(j,end=" ")
#     print()

# # # 1
# # # 2 2
# # # 3 3 3
# # # 4 4 4 4
# for i in range(1,4):
#     for j in range(i):
#         print(i,end=" ")
#     print()


# #1
# #1 2
# #1 2 3

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# #1
# #2 1
# #3 2 1
# # 4 3 2 1 
# a=1
# for i in range(1,5):
#     for j in range(i):
#         print (a-j,end=" ")
#     print()
#     a=a+1


# *
# **
# ***   
# ****
# *****
# ****
# ***
# **
# *
n=5
for i in range(n):
    for j in range(i):
        prind("*",end=" ")
    print()