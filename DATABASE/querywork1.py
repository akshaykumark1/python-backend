# create new data base 
import sqlite3
con=sqlite3.connect("new.db")
try:
    con.execute('create table u_details(user_id int,user_name text,user_email text,user_number)')
except:
    pass
# con.execute('insert into u_details(user_id,user_name,user_email,user_number) values(4,"vinash","vinashi@123",1234567890)')
# con.execute('delete from u_details where user_id=4')
#con.execute('select count(user_id) from u_details')
# con.execute('select * from u_details where user_id=1')
#con.execute('select sum(user_id) from u_details')
#con.execute('select avg(user_id) from u_details')
#con.execute('select max(user_id) from u_details')
#con.execute('select min(user_id) from u_details')

for i in data:
    print(i)
    # print("{:<2} {:<10} {:20} {:10}".format(i[0], i[1], i[2], i[3]))
con.commit()
