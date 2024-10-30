# input  sets
# common in python and java
# comon in java and php
# common in all batches
# print un common in all batch

set1=python={"akshay","agu","vinayak"}
set2=java={"akshay","hydi","kim"}
set3=php={"akshay","art","hello"}
print(""" 
1. Common in set 1 and set 2
2. Common in set 2 and set 3
3. Common in all sets
4. Uncommon in all sets            
""")
choice = int(input("Enter your choice: "))

if choice == 1:
    print(set1.intersection(set2))
elif choice == 2:
    print(set2.intersection(set3))
elif choice == 3:
    print(set1.intersection(set2, set3))
elif choice == 4:
    u=(python.union(java,php))
    a=(python.intersection(java))
    b=(java.intersection(php))
    s=u.difference(a,b)   
    print(s)
else:
    print("Invalid choice")
