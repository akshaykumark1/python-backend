#  *
# * *
#* * *
# for i in range(3):  # iterates over the rows
#     for j in range(2-i):  # prints leading spaces for each row
#         print(" ", end=" ")
#     for k in range(i+1):  # prints asterisks for each row
#         print("* ", end=" ")
#     print()  # moves to the next line after each row


# The outer loop determines the number of rows in the pyramid
# The first inner loop prints the leading spaces for each row
# The second inner loop prints the asterisks for each row
# The number of spaces and asterisks is determined by the
# current row number and the total number of rows

#output
#    *
#   ***
#  *****
# This code generates a pyramid pattern of asterisks
# The number of rows in the pyramid is determined by the outer loop

# for i in range(4):  # iterates over the rows
#     for j in range(3-i):  # prints leading spaces for each row
#         print(" ", end=" ")
#     for k in range(2*i-1):  # prints asterisks for each row
#         print("*", end=" ")
#     print()  # moves to the next line after each row



# count=65
# for i in range(4):
#     for j in range(4):
#         print(chr(count),end=" ")
#         count=count+1
#     print()

    # output:    ASCII VALUE OF A IS 65 THEN INCREMENT BY 1
    # A B C D 
    # E F G H 
    # I J K L 
    # M N O P
