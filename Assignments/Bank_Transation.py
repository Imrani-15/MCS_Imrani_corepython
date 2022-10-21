import sys
class Customer:
    Bankname = "ICIC BANK"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance+amt
        print("Balance after deposite",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficienct balance.... cannot perform this operation")
            sys.exit()
        self.balance = self.balance-amt
        print('Balance after withdraw:',self.balance)
print("Welcome to",Customer.Bankname)
name = input("Enter the customer name:")
deposit = int(input("what amt Deposit the amount to your amount:: "))
withdraw = int(input("what amt Withdraw the amount:: "))

print("\nWelcome to ICIC BANK:",name)
print(name,"ICIC BANK TRANSCATIONS")
c = Customer(name)
c.deposit(deposit)
c.withdraw(withdraw)
# tiyango