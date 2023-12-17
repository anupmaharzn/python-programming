

class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"accout owner:{self.owner}\n account balance:{self.balance}"

    def deposite(self,amount):
        self.balance +=amount
        print('deposit acccepted')
        return self.balance
    
    def withdraw(self,amount):
        if self.balance < amount:
            return print('Funds unavialable!')
        
        else:
            self.balance -=amount
            return self.balance
        

acct1 = Account('jose',100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposite(100)
print(acct1.balance)

acct1.withdraw(500)

acct1.withdraw(50)
print(acct1.balance)

