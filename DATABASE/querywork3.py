# create table student details and user input can update,delete,search the student details using while true
import sqlite3
con = sqlite3.connect("std.db")
try:
    con.execute('CREATE TABLE std_details(std_admno INT, std_name TEXT, std_email TEXT, std_adress TEXT)')
except:
    pass
# limit = int(input("Enter the number of students: "))

while True:
    print("1.insert\n2.update\n3.delete\n4.search\n5.exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        std_admno = int(input("Enter the admission number: "))
        std_name = input("Enter the student name: ")
        std_email = input("Enter the email: ")
        std_adress = input("Enter the address: ")
        con.execute('INSERT INTO std_details(std_admno, std_name, std_email, std_adress) VALUES (?, ?, ?, ?)', 
                    (std_admno, std_name, std_email, std_adress))
        con.commit()

    elif choice == 2:
        std_admno = int(input("Enter the admission number: "))
        cursor = con.execute('SELECT * FROM std_details WHERE std_admno = ?', (std_admno,))
        data = cursor.fetchone()
        if data:
            print("Record found. Enter new data to update.")
            std_name = input("Enter the student name: ")
            std_email = input("Enter the email: ")
            std_adress = input("Enter the address: ")
            con.execute('UPDATE std_details SET std_name = ?, std_email = ?, std_adress = ? WHERE std_admno = ?', 
                        (std_name, std_email, std_adress, std_admno))
            con.commit()
        else:
            print("Record not found.")

    elif choice == 3:
        std_admno = int(input("Enter the admission number: "))
        cursor = con.execute('SELECT * FROM std_details WHERE std_admno = ?', (std_admno,))
        data = cursor.fetchone()
        if data:
            con.execute('DELETE FROM std_details WHERE std_admno = ?', (std_admno,))
            con.commit()
            print("Record deleted.")
        else:
            print("Record not found.")

    elif choice == 4:
        std_admno = int(input("Enter the admission number: "))
        cursor = con.execute('SELECT * FROM std_details WHERE std_admno = ?', (std_admno,))
        data = cursor.fetchone()
        if data:
            print("Record found:", data)
        else:
            print("Record not found.")
            
    elif choice == 5:
        break

con.close()


