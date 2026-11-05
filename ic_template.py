# ウチダ電鉄　UchICaチャージ機能検証システム
# ・charge関数とmain関数を、設計書を参考に完成させてください。
# ・関数名は変更しないでください。


def charge(money):
    # ここにcharge関数の処理を書いてください
    # 引数と戻り値に何を指定するかは設計書から判断してください
    charges =[]
    for i in range(1, 10000, 1000):
        charges.append(i)

    print("チャージ機能")
    print(f"チャージ残高は{money}です")
    for i in range(len(charges)):
        print(f"{i+1}: {charges[i]}円")
    choice = int(input("チャージする金額を選択してください（番号で入力1~10(1000円単位））: キャンセルする場合には99を入力してください "))
    if choice < 1 or choice > len(charges):
        print("無効な選択です。もう一度やり直してください。")
        return money
    elif choice ==99:
        print("チャージをキャンセルしました。")
        return money

    money += charges[choice - 1]
    print(f"チャージが完了しました。現在の残高: {money}円")
    return money


def main():
    # ここにmain関数の処理を書いてください
    # 引数と戻り値に何を指定するかは設計書から判断してください
    balance =500
    while balance < 20000:
        balance = charge(balance)
    print("チャージ可能金額を超えたため、システムを終了します。")

if __name__ == "__main__":
    main()
