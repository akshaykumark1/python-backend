# importing sqlite 3
import sqlite3
con=sqlite3.connect("user.db")
try:
    con.execute('create table u_details(user_id int,user_name text,user_email text,user_number, text)')
except:
    pass
con.execute('insert into u_details(user_id,user_name,user_email,user_number) values(1,"sudhanshu","sudhanshu@123",1234567890)')
con.commit()