# print largest word in list
a=["apple","kiwi","orange"]

# initialize bigg with first element of the list
bigg=a[0]
small=a[0]
# loop through the list
for i in a:
    # if the length of the current element is less than the length of bigg
    if len(i)<len(bigg):
        print(bigg)
    else:
        if len(i)>len(small):
            print(small)


        # update bigg with the current element
    

# print the largest word