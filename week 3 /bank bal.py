def credit(balance,value):
    balance=balance + value
    return balance
def debit(balance,value):
    balance=balance - value
    return balance
def showbalance(balance):
    print(balance)
    
    
    
balance=0
balance=credit(balance,5000)
balance=debit(balance,1500)
showbalance(balance)
