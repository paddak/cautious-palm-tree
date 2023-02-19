#다이아몬드 상속

class A:
    def greeting(self):
        print("A안녕!")

class B(A):
    def greeting(self):
        print("B안녕!")

class C(A):
    def greeting(self):
        print("C안녕!")

class D(B,C):
    pass

print(D.mro())  #D(B,C)에서 왼쪽먼저 호출
x=D()
x.greeting()    