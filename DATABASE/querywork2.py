# input student details in sqlite3
import sqlite3
con=sqlite3.connect("student.db")
try:
        con.execute('create table std_details(std_admno int,std_name text,std_email text,std_totmarks int)')
except:
        pass
limit=int(input("enter the number of students: "))
for i in range(limit):
    print("student :",i+1)
    std_admno=int(input("enter the admission number: "))
    std_name=input("enter the student name: ")
    std_email=input("enter the email: ")
    std_totmarks=int(input("enter the total marks: "))
con.execute('insert into std_details(std_admno,std_name,std_email,std_totmarks) values(?,?,?,?)',(std_admno,std_name,std_email,std_totmarks))
con.commit()
# con.execute('update std_details set std_name="vinu" where std_admno=112')
# con.execute('select count(*) from std_details')
# con.execute('select sum(*) from std_details')
# con.execute('select avg(*) from std_details')
# con.execute('select max(*) from std_details')
# data=con.execute('select min(*) from std_details')

# for i in data:
#     print(i)
# con.commit()



