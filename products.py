products = []

while True:
    product = input("請輸入商品名稱：(q for quit)")
    if product == "q":
        break
    price = int(input("請輸入價格："))
    p = [product, price] #建立小清單
    products.append(p) #將小清單列入打清單

print(products) #印出打清單

for p in products: #用for loop一條一條地印出大清單中的資料（小清單）
    print(p)

#寫入檔案
with open("products.csv", "w", encoding="utf-8") as f: #有沒有檔案都沒關係，沒有的話會自動新增 #副檔名txt>csv #加入encoding編碼
    f.write("商品,價格\n") #在數據前先寫入欄位名稱
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n") #用"," 比較適合excel #str()將int轉換成字串