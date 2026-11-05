def charge(balance):
    availablePrices = range(1000, 10001, 1000)

    print("【チャージ機能】")
    print(f"チャージ残高は{balance}円です。")

    for i in range(len(availablePrices)):
        print(f"{i + 1}: {availablePrices[i]} 円")

    print("チャージする金額を選択してください(キャンセルする場合には99を入力)")

    while True:
        try:
            choice = int(input())
            if choice == 99:
                print("チャージをキャンセルしました．")
                print(f"チャージ残高は{balance}円です．\n\n")
                break;
            elif 1 <= choice <= len(availablePrices):
                balance += availablePrices[choice - 1]
                print(f"{availablePrices[choice - 1]}円をチャージします．")
                print(f"チャージ残高は{balance}円です．\n\n")
                break;
            else:
                raise ValueError
        except ValueError:
            print("正しい数値を入力してください．")
    return balance

def main():
    balance = 500
    while balance <= 20000:
        balance = charge(balance)
    print("チャージ残高が20000円を超えたため，システムを終了します．")


if __name__ == "__main__":
    main()