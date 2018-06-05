coffee = 10
price = 300



while coffee >= 0:
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break
    user1 = int(input("동전 투입: "))
    if user1 < price:
        print("돈을 다시 돌려 줍니다.")
        print("남은 커피의 양은 {} 잔 입니다.". format(coffee))
    elif user1 == price:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif user1 > price:
        print("거스름돈{}원과 커피를 줍니다".format(user1-price))
        coffee = coffee -1