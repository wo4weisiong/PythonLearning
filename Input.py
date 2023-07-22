name = input("您好，請問您是：")
print("歡迎光臨肌動健身房,",name,"接下來將先為您測量身高和體重")
height = float(input("您的身高（米）："))
# print("身高（米）：",height,"m")
weight = int(input("您的體重（公斤）："))
# print("體重（公斤）：",weight,"Kg")

bmi = weight/(height**2) #BMI公式
print("身高：",height,"m","  ","體重：",weight,"Kg")
print("您的BMI:",bmi)