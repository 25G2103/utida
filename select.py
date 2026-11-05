def select_stations():
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]
    print("[乗車駅選択]")
    for i in range(len(stations)):
        print(f'{i+1}: {stations[i]}駅まで{fares[i]}円です')
    while True:
        try:
            destination = int(input("乗車駅を選択してください（番号で入力1~3）: キャンセルする場合には99を入力してください "))
            if destination == 99:
                print("乗車選択をキャンセルしました")
                return 0
            elif 1 <= destination <= len(stations):
                break
            else:
                print("正しい数値を入力してください")
        except ValueError:
            print("正しい数値を入力してください")

    print(f'{stations[destination-1]}で料金は{fares[destination-1]}円です。')
    return fares[destination-1]

if __name__ == "__main__":
    print("戻り値:", select_stations())