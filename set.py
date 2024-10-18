# set
# set is an unordered collection of elements
# set is immutable
# set is a collection of unique elements
# set is unordered
# set is mutable
# #set add
# set={1,2,3,4,5}
# set.add(6)
# print(set)

# #set update
# set={1,2,3,4,5}
# set.update({6,7,8})
# print(set)

# # #set remove
# set={1,2,3,4,5}
# set.remove(2)
# print(set)


# #set pop
# set={1,2,3,4,5}
# set.pop(2)
# print(set)



# set discard
# set={1,2,3,4,5}
# set.discard(6)
# print(set)


#common methods
a={1,2,3,4,5,6,7}
b={1,2,3,4,5}
print(a.difference(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.symmetric_difference(b))
a.difference_update(b)
print(a)
a.intersection_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)