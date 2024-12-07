# bank accout user input = deposit and withdraw ,and check balance using class and object

class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance+=amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:",amount)
        else:
            print("\n Insufficient balance ")
    def display(self):
        print("\n Net Available Balance=",self.balance)

# obj1=BankAccount()
# obj1.deposit()
# obj1.withdraw()
# obj1.display()

account1=BankAccount()
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        account1.deposit()
    elif choice=="2":
        account1.withdraw()
    elif choice=="3":
        account1.display()
    elif choice=="4":
        break
    else:
      print("Invalid choice")

