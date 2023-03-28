class Account:

    def __init__(self, title=None,balance=0):
        self.title=title
        self.balance=balance
        
    def withdrawal(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount
        
    def getBalance(self):
        return self.balance
    

class SavingsAccount(Account):
    
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance*self.interestRate/100)


demo1 = SavingsAccount("jangam gouthami yadav", 6000, 7)

print(demo1.title, demo1.balance, demo1.interestRate, sep=" ")

demo1.deposit(int(input("enter the deposit amount :")))

demo1.withdrawal(int(input("enter the withdrawl amount :")))

print("your balance",demo1.getBalance())

print("interest:",demo1.interestAmount())


jangam gouthami yadav 6000 7
enter the deposit amount :7000
enter the withdrawl amount :2000
your balance 11000
interest: 770.0