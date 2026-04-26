import storage 
def withdraw_money():
    amount=float(input("enter amount : "))
    if(amount>storage.balance):
        print("unsufficient balance")
    else:
        storage.balance-=amount
        storage.transactions.append(f"withdrawn:{amount}")
    
    
