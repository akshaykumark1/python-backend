# find  letter a in list
# l=["apple","orange","kiwi"]
# for i in l:
#     if "a" in i:
#         print(i)


# using filter
l=["apple","orange","kiwi"]
letter=(input("enter the letter: "))
# print(list(filter(lamda a:letter in a,l)))
data=filter(lambda a:letter in a,l)
print(list(data))    