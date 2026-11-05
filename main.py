def main():
    balance = 500

    while True:
        import menu  #統合後に削除する
        selected = menu.menu()

        if selected == 1:
            import selectStation  #統合後に削除する
            fare = selectStation.selectStation()
            if fare != 0:
                import pay  #統合後に削除する
                balance = pay.pay(balance, fare)

        elif selected == 2:
            import charge  #統合後に削除する
            balance = charge.charge(balance)
        elif selected == 99:
            print("システムを終了します。")
            break;


if __name__ == "__main__":
    main()