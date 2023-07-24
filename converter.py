#攝氏（'C）轉換成華氏（'F）

temp_c = float(input("請輸入攝氏溫度（'C）："))

temp_f = temp_c*(9/5)+32

if temp_f >= 100:
    print("今天非常熱：",temp_f,"'F")
elif temp_f <= 50:
    print("今天很冷：",temp_f,"'F")
else:
    print("今天天氣很好：",temp_f,"'F")
