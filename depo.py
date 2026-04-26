import storage
def deposit_money():
    amount=float(input("enter amount: "))
    storage.balance+=amount
    storage.transactions.append(f"deposited:{amount}")
