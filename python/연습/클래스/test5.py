# class Person:
#     bag=[]                            #클래스속성 모두가 공유
    
#     def put_bag(self,stuff):
#         self.bag.append(stuff)

# james=Person()
# james.put_bag("책")
# print(james.bag)

# peter=Person()
# peter.put_bag("열쇠")
# print(peter.bag)                      

class Person:
    def __init__(self):
        self.bag=[]                     #인스턴스속성 콜한 인스턴스만씀
    
    def put_bag(self,stuff):
        self.bag.append(stuff)
    
james=Person()
james.put_bag("책")

maria=Person()
maria.put_bag("열쇠")

print(james.bag)
print(maria.bag)