# password validation
import re
password=input("enter the password")
x="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
if re.search(x,password):
    print("valid password")
else:
    print("invalid password")
    
    