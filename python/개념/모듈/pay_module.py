version=2.0

def printAuthor():
    print("스타트코딩")

class Pay:
    def __init__(self,id,price,item):
        self.id=id
        self.price=price
        self.item=item
    
    def get_pay_info(self):
        return f"{self.id} {self.time} {self.item}"
    
#해당파일 직접실행했을때만 실행   
if __name__=="__main__":
    print("pay module 실행")

print(__name__)