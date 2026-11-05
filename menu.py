def menu():
    function = ["乗車駅選択","チャージ機能"]
    print("ウチダ電鉄　交通系ICカード検証システム")
    for i in range(len(function)):
        print(f"{i+1}:{function[i]}")
        
    print("使用する機能を入力してください(終了する場合には99を入力)")

    a = int(input("番号を入力"))
    return a


def main():
    menu()

if __name__ == "__main__":
    main()