from bal import display_balance
from wthrw import withdraw_money
from depo import deposit_money
from trns import show_trans
while True:
    print("\n1. Display Balance")
    print("\n2. Withraw Money")
    print("\n3. Deposit Money")
    print("\n4. show Transactions")
    print("\n5. exit")


    choice=input("enter your choice: ")
    if(choice=="1"):display_balance()
    elif(choice=="2"):withdraw_money()
    elif(choice=="3"):deposit_money()
    elif(choice=="4"):show_trans()
    elif(choice=="5"):
        print("Thank you for using ATM")
        break

    else:print("invalid choice try again")
