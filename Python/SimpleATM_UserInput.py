#Mock ATM UI

user_Account = {"balance": "237", "pin": "2853"}
pin_attempt = 0
def waiting():
    input("Input Card: ")
    pin_entry(pin_attempt)

def pin_entry(tries):
    if tries < 3:
        pin_entered = input("Enter your Pin: ")
        if str(pin_entered) == user_Account["pin"]:
            account_features()
        else:
            tries += 1
            print("Incorrect Pin")
            pin_entry(tries)
    else: 
        print("Too Many Failed Attempts")
        transaction_ended()

def account_features():
        if user_Account["balance"] == 0:
            print("Account Closed")
            transaction_ended()
        else:
            withdraw_amount = input("Enter Withdrawal Amount: ")
            try:
                if float(withdraw_amount) > float(user_Account["balance"]):
                    print("Insufficient Funds")
                    print("Balance: "+user_Account["balance"])
                    account_features()
                else:
                    print("Cash Dispensing\n")
                    user_Account["balance"] = str(float(user_Account["balance"])-float(withdraw_amount))
                    print("New Balance: "+user_Account["balance"])
                    transaction_ended()
            except:
                print("Invalid Entry: Try Again")
                account_features()

def transaction_ended():
    print("Returning Card")
    print("Transaction Ended\n")
    waiting()

waiting()