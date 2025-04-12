balance=0
transaction=[]

def credit(amount):
    global balance
    balance  += amount
    transaction.append(amount)
    print("AMOUNT CREDIT SUCCESSFULLY")
    
def debit(amount):
    global balance
    if amount > balance:
        print("INSUFFICIENT BALANCE")
    else:
        balance -=amount
        print("AMOUNT DEBBITED SUCCESSFULLY")
    
def show_balance():
    print(balance)
    
def last_transactions(amount):
    print("LAST % TRANSCATIONS:")
    for t in transaction[-5:]:
        print(t)
        print()
    
    
while True:
    print("1. Press 1 for credit amount")
    print("2. Press 2 for debit amount")
    print("3. Press 3 for show balance")
    print("4. Press 4 for last 5 transactions")
    
    choice=int(input("ENTRE YOUR CHOICE:"))
    if choice==1:
        amount=int(input("Entre the amount to br credited:"))
        credit(amount)
    elif choice==2:
            amount = int(input("Entre the amount to be debited:"))
            debit(amount)
    elif choice ==3:
        show_balance()
    elif choice ==4:
        last_transactions()

              
          
               
    
    

    
