from MenuDemandAll import *
menu=MenuDemandAll()
menu.loadMenu()
menu.loadDemands()
class StepsAll:
    def milk_tea_steps(self,name) :
        print('准备杯子,正在加热奶,正在注入茶水,加入'+menu.menu["MilkTea"][0][name])
    
    def fruit_tea_steps(self,name) :
        print("准备杯子,正在加热奶,正在注入茶水,加入"+menu.menu["JuiceTea"][0][name])

    def pure_tea_steps(self,name) :
        print("准备杯子,正在加热奶,正在注入茶水,加入"+menu.menu["Tea"][0][name])

    def juice_steps(self,name) :
        print("准备杯子,正在加热奶,正在注入茶水,加入"+menu.menu["Juice"][0][name])