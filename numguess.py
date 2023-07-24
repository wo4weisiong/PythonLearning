#猜數字遊戲

import random #random是一個模組 #載入模組

r = random.randint(1,100)
while True:
    guess = int(input("請輸入數字"))
    if guess == r:
        print("恭喜你答對了")
        break
    elif guess != r:
        if guess <= r:
            print("比",guess,"大")
        elif guess >= r:
            print("比",guess,"小")