# student details 
# admission number,name,age,course
# add student,delete student,search student,show all student,exit

students = {}

while True:
    print("1. Add student")
    print("2. Delete student")
    print("3. Search student")
    print("4. Show all student")
    print("5. Exit")
    choice = int(input("Enter your ,.choice: "))

    if choice == 1:
        admission_number = input("Enter admission number: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        students[admission_number] = {"name": name, "age": age, "course": course}
        print("Student added successfully")
    elif choice == 2:
        admission_number = input("Enter admission number to delete: ")
        if admission_number in students:
            del students[admission_number]
            print("Student deleted successfully")
        else:
            print("Admission number not found")
    elif choice == 3:
        admission_number = input("Enter admission number to search: ")
        if admission_number in students:
            print("Student found")
            print("Name: ", students[admission_number]["name"])
            print("Age: ", students[admission_number]["age"])
            print("Course: ", students[admission_number]["course"])
        else:
            print("Admission number not found")
    elif choice == 4:
        print("List of all students: ")
        for admission_number in students:
            print("Admission number: ", admission_number)
            print("Name: ", students[admission_number]["name"])
            print("Age: ", students[admission_number]["age"])
            print("Course: ", students[admission_number]["course"])
            print()
    elif choice == 5:
        break
    else:
        print("Invalid choice")



