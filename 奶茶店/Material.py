from MenuDemandAll import *
menu=MenuDemandAll()
menu.loadMenu()
menu.loadDemands()
class Material:
    def __init__(self, name,temperature,sweet,size,numbers):
        self.name = name
        self.size = size
        self.temperature=temperature
        self.sweet=sweet
        self.numbers=numbers
        self.requirements = {}

    def use_materials(self,materials):
        for material, quantity in self.requirements.items():
            if material in materials and materials[material] >= quantity:
                materials[material] -= quantity
            else:
                print("「{}」制作失败，库存不足！".format(self.name))
                return False

        return True
class MilkTea(Material):
    def __init__(self, name,temperature,sweet, size,numbers):
        super().__init__(name,temperature,sweet, size,numbers)
        if menu.isMilkTea(name) :
            if  size=="大杯":
                self.requirements = {
                    "普通红茶": 3*numbers,
                    "牛奶": 60*numbers,
                    menu.menu["MilkTea"][0][name]:6*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }
            else:
                self.requirements={
                    "普通红茶":2*numbers,
                    "牛奶":40*numbers,
                    menu.menu["MilkTea"][0][name]:4*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }

class JuiceTea(Material):
    def __init__(self, name,temperature,sweet, size,numbers):
        super().__init__(name,temperature,sweet, size,numbers)
        if menu.isJuiceTea(name):
            if size=="大杯":
                self.requirements = {
                    "普通红茶": 3*numbers,
                    menu.menu["JuiceTea"][0][name]:6*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }
            else:
                self.requirements={
                    "普通红茶":2*numbers,
                    menu.menu["JuiceTea"][0][name]:4*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }

class Tea(Material):
    def __init__(self, name,temperature,sweet, size,numbers):
        super().__init__(name,temperature,sweet, size,numbers)
        if menu.isTea(name):
            if size=="大杯":
                self.requirements = {
                    menu.menu["Tea"][0][name]:6*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }
            else:
                self.requirements={
                    menu.menu["Tea"][0][name]:4*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }

class Juice(Material):
    def __init__(self, name,temperature,sweet, size,numbers):
        super().__init__(name,temperature,sweet, size,numbers)
        if menu.isJuice(name):
            if  size =="大杯":
                self.requirements = {
                    menu.menu["Juice"][0][name]:6*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }
            else:
                self.requirements={
                    menu.menu["Juice"][0][name]:4*numbers,
                    "冰块":menu.demands["温度"][0][temperature]*numbers,
                    "糖浆":menu.demands["甜度"][0][sweet]*numbers
                }