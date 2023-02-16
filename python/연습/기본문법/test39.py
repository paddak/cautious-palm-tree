class Person:
    bag=[]
    
    def __init__(self,stuff):
        self.stuff=stuff
    
    def put_bag(self):
        self.bag.append()

james=Person()
james.put_bag("책")

maria=Person()
maria.put_bag("열쇠")

print(james.bag)