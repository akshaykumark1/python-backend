# add an element in tuple

a=(1,2,3,4,5,6,7,8,9,10)
b=list(a)
b.extend([11,12])
a=tuple(b)
print(a)
