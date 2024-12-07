try:
    with open("task.txt", "r") as f:
        b = f.read().splitlines()
except FileNotFoundError:
    b = []

while True:
    print(""" 
             1.add
             2.view
             3.delete
             4.exit""")
    choice = input("Enter your choice: ")

    if choice == "1":
        b.append(input("Enter name: "))
    elif choice == "2":
        print(b)
    elif choice == "3":
        name = input("Enter name: ")
        if name in b:
            b.remove(name)
        else:
            print("Name not found")
    elif choice == "4":
        with open("task.txt", "w") as f:
            f.write(str(b))
        break
