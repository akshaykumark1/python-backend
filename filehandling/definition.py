# modes in file handling
# r - open for reading only
# w - open for writing only
# a - open for appending
# x - open for exclusive creation

# syntax;
# f = open("filename","mode")
# f = open("hlo.txt",'x')
f = open("hlo.txt",'w')
f.write("hi")