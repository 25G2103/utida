def pay(balance, fare):
    print(f"チャージ残高は{balance}円です。")
    if fare > balance:
        print("残高不足です。")
        #Auto Charge
        while balance <= fare:
            balance += 3000
            print("3000 円自動チャージします。")
    
    #Pay
    balance -= fare
    print(f"精算後のチャージ残高は{balance}円です。")
    if balance < 500:
        balance += 3000
        print("残高が500 円未満のため3000 円自動チャージします。")
        print(f"チャージ残高は{balance}円です。")

    return balance
