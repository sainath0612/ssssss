import sys
class customer:
    bankname="STATE BANK OF INDIA"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("the balance after deposit :",self.balance)
    def withdraw(self,amount):
        if amount >=50000:
            print("Over limit amount per day ")
            sys.exit()
        if amount > self.balance:
            print("insufficient amount in account ....... plz check the balance")
            sys.exit()
        self.balance=self.balance-amount
        print("the remaining balance after withdraw :",self.balance)
print("WELCOME TO :",customer.bankname)
name=input("enter your name :")
c=customer(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-Exit ")
    option=input("enter the option :").lower()
    if option=='d':
        amount=float(input("enter the deposit amount:"))
        c.deposit(amount)
    elif option=="w":
        while True:
            amount=float(input("enter the withdraw amount:"))
            if not(amount>0 and amount%100==0):
                print("the amount you enter to be in hundreds")
            else:
                break
        c.withdraw(amount)
    elif option=="e":
        print("Thanks for choosing STATE BANK OF INDIA")
        break
    else:
        print("the enter option is wrong plz check while entering")



