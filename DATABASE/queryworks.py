import sqlite3
con=sqlite3.connect("user.db")
y# for i in range(limit):
#     name=input("enter the name")
#     email=input("enter the email")
#     number=int(input("enter the number"))
#     con.execute('insert into u_details(user_id,user_name,user_email,user_number) values(?,?,?)',(name,email,number))
con.execute("update u_details set user_name='vinu' where user_id=4")
con.commit()    

