class Item:
    def __init__(self,name,price,weight,isdropable):
        self.name=name
        self.price=price
        self.weight=weight
        self.isdropable=isdropable
    
    def sale(self):
        print(f"{self.name} 판매가격은 {self.price}")
    
    def discard(self):
        if (self.isdropable):
        # if (self.isdropable==True):
            print(f"{self.name} 버린다")
        else:
            print("못버린다")

class WeareableItem(Item):
    def __init__(self, name, price, weight,isdropable,effect):
        super().__init__(name, price, weight,isdropable)
        self.effect=effect
    def wear(self):
        print(f"{self.name} 착용했당 {self.effect}")

class UseableIterm(Item):
    def __init__(self, name, price, weight,isdropable,effect):
        super().__init__(name, price, weight,isdropable)
        self.effect=effect
    def use(self):
        print(f"{self.name} 사용했다. {self.effect}")


nike=WeareableItem("나이키",30000,50,True,"반짝반짝")
nike.wear()
nike.sale()
nike.discard()

coke=UseableIterm("콜라",4000,1,False,"꿀꺽")
coke.use()

