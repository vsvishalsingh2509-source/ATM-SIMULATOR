from storage import transactions
def show_trans():
    if(len(transactions)==0):
        print("no transactions made")
    else:
        for _ in transactions:
            print(_)    