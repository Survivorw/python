import numpy as np
from 奶茶店.Material import *
from 奶茶店.MenuDemandAll import *
from 奶茶店.procedure import *
S=StepsAll()
menu=MenuDemandAll()
menu.loadDemands()
menu.loadMenu()
print("欢迎来到鸡哥奶茶店")
print("以下为目录")
print("MilkTea:芋圆奶茶","珍珠奶茶","珍珠烤奶",
      "夏日奶茶","奥利奥奶茶","布丁奶茶","红豆奶茶",
      "椰子奶茶","西米奶茶","烤奶茶")
print("Tea:乌龙茶","大红袍","茉莉花茶",
      "铁观音","普洱茶","绿茶",
      "龙井茶","红茶","菊花茶","白茶")
print("JuiceTea:杨枝甘露","草莓奶冻","柠檬绿茶",
      "柠檬红茶","生椰西瓜","西瓜啵啵","芒果奶茶",
      "草莓麻薯","超级水果茶","芒果杨枝甘露")
print("Juice:西瓜汁","草莓汁","橙汁",
      "柠檬水","橘子汁","雪梨汁","芒果汁",
      "葡萄汁","柚子汁","椰子汁")
print("请按固定格式选择你的奶茶口味，规格，温度，甜度，是否打包（是/否），数量")

cha=input()
cha_list=cha.split()


if menu.isJuice(cha_list[0]) or menu.isJuiceTea(cha_list[0]) or menu.isMilkTea(cha_list[0]) or menu.isTea(cha_list[0]):
    if menu.isSize(cha_list[1]) and menu.isTemperature(cha_list[2]) and menu.isSweet(cha_list[3]) and menu.isPack(cha_list[4]):
        pass
    else:print("您输入的需求格式错误，请重新输入")
else:
    print("您输入的产品不存在，请重新输入")

if menu.isJuice(cha_list[0]):
      M=Juice(cha_list[0],cha_list[2],cha_list[3],cha_list[1],(int)(cha_list[5]))
      S.juice_steps(cha_list[0]) 
if menu.isJuiceTea(cha_list[0]):
      M=JuiceTea(cha_list[0],cha_list[2],cha_list[3],cha_list[1],(int)(cha_list[5]))
      S.fruit_tea_steps(cha_list[0])
if menu.isMilkTea(cha_list[0]):
      M=MilkTea(cha_list[0],cha_list[2],cha_list[3],cha_list[1],(int)(cha_list[5]))
      S.milk_tea_steps(cha_list[0])
if menu.isTea(cha_list[0]):
      M=Tea(cha_list[0],cha_list[2],cha_list[3],cha_list[1],(int)(cha_list[5]))
      S.pure_tea_steps(cha_list[0])

materials = {"牛奶": 1000, "糖浆": 100,"冰块": 1000,
             "珍珠":100,"芋圆":100,
             "草莓":100,"西瓜":100,"椰子":100,
             "橘子":100,"西米":100,"葡萄":100,
             "柚子":100,"柠檬":100,"橙子":100,
             "红豆":100,"雪梨":100,"芒果":100,
             "奥利奥":100,"龙井茶":100,"茉莉花茶":100,
             "普洱茶":100,"铁观音":100,"绿茶":100,
             "菊花茶":100,"白茶":100,"乌龙茶": 100,
             "大红袍": 100,"普通红茶":100}

class OrderSystem:
    def __init__(self, materials):
        self.materials = materials
        self.drinks = []

    def add_drink(self, drink):
        if drink.use_materials(materials):
            self.drinks.append(drink)

    def checkout(self):
        # 打印订单信息和库存状态
        print("您的饮品制作已完成，请提取：")
        for drink in self.drinks:
            print(drink.name)
        #print("总价：", self.total_price)

        # 检查库存状态
        print("当前原材料库存：")
        for material, quantity in self.materials.items():
            print(material, quantity)
            if quantity <= 0:
                print("【警告】「{}」已经没有库存了！".format(material))


order_system = OrderSystem(materials)

order_system.add_drink(M)
order_system.checkout()


