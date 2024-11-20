# email validation
import re
email=input("enter the email: ")
pattern="[a-z0-9]+[@]+[gmail]+[.]+[com]"
if re.search(pattern,email):
    print("valid email")
else:
    print("invalid email")