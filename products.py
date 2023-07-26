products = []

while True:
    product = input("請輸入商品名稱：(q for quit)")
    if product == "q":
        break
    price = input("請輸入價格：")
    p = [product, price] #建立小清單
    products.append(p) #將小清單列入打清單

print(products) #印出打清單

for p in products: #用for loop一條一條地印出大清單中的資料（小清單）
    print(p)

#寫入檔案
with open("products.csv","w") as f: #有沒有檔案都沒關係，沒有的話會自動新增 #副檔名txt>csv
    for p in products:
        f.write(p[0] + "," + p[1] + "\n") #用"," 比較適合excel