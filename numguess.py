#猜數字遊戲

import random #random是一個模組 #載入模組

setup_start = int(input("請輸入開始值："))
setup_end = int(input("請輸入結束值："))

r = random.randint(setup_start,setup_end)
count = 0
while True:
    count = count + 1 #也可以寫成 count += 1
    guess = int(input("請輸入數字："))
    if guess == r:
        print("恭喜你答對了,共用了",count,"次機會")
        break
    elif guess != r:
        if guess <= r:
            print("比",guess,"大")
        elif guess >= r:
            print("比",guess,"小")
    print("這是你猜的第",count,"次")