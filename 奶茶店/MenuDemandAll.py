class MenuDemandAll:
      menu=dict()
      demands=dict()
      def loadMenu(self):
          self.menu["MilkTea"]=[{"芋圆奶茶":"芋圆","珍珠奶茶":"珍珠","珍珠烤奶":"珍珠",
                                 "夏日奶茶":"西米","奥利奥奶茶":"奥利奥","布丁奶茶":"布丁",
                                 "红豆奶茶":"红豆","椰子奶茶":"椰子","西米奶茶":"西米","烤奶茶":"珍珠"}]
          self.menu["Tea"]=[{"乌龙茶":"乌龙茶","大红袍":"大红袍","茉莉花茶":"茉莉花茶","铁观音":"铁观音","普洱茶":"普洱茶","绿茶":"绿茶","龙井茶":"龙井茶","普通红茶":"普通红茶","菊花茶":"菊花茶","白茶":"白茶"}]
          self.menu["JuiceTea"]=[{"杨枝甘露":"芒果","草莓奶冻":"草莓","柠檬绿茶":"柠檬",
                                 "柠檬红茶":"柠檬","生椰西瓜":"西瓜","西瓜啵啵":"西瓜",
                                 "芒果奶茶":"芒果","草莓麻薯":"草莓","超级水果茶":"西瓜","芒果杨枝甘露":"芒果"}]
          self.menu["Juice"]=[{"西瓜汁":"西瓜","草莓汁":"草莓","橙汁":"橙子",
                               "柠檬水":"柠檬","橘子汁":"橘子","雪梨汁":"雪梨","苹果汁":"苹果",
                               "葡萄汁":"葡萄","柚子汁":"柚子","椰子汁":"椰子"}]
      def isMilkTea(self,dish):
          if dish in self.menu["MilkTea"][0]:
              return True
          return False
      def isTea(self,dish):
          if dish in self.menu["Tea"][0]:
              return True
          return False
      def isJuiceTea(self,dish):
          if dish in self.menu["JuiceTea"][0]:
              return True
          return False
      def isJuice(self,dish):
          if dish in self.menu["Juice"][0]:
              return True
          return False
      def loadDemands(self):
          self.demands["温度"]=[{"常温":0,"去冰":0,"加冰":5,"热":0}]
          self.demands["甜度"]=[{"半糖":5,"全糖":10,"七分糖":7,"无糖":0}]
          self.demands["规格"]=["大杯","中杯"]
          self.demands["打包"]=["是","否"]
      def isTemperature(self,Temperature):
          if Temperature in self.demands["温度"][0]:
              return True
          return False
      def isSweet(self,Sweet):
          if Sweet in self.demands["甜度"][0]:
              return True
          return False
      def isSize(self,Size):
          if Size in self.demands["规格"]:
              return True
          return False
      def isPack(self,Pack):
          if Pack in self.demands["打包"]:
              return True
          return False