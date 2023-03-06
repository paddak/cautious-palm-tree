#__getitem__ 메서드 사용하여 인덱스로 접근할 수 있는 이터레이터

class Ex_Iterator:
    def __getitem__(self, 인덱스):
        pass

class Counter:                  #__iter__,__next__이용해서 이터레이터 구현했는데 __getitem__쓰면 생략가능(초기값도 없다면 __init__ 생략가능)
    def __init__(self,stop):
        self.stop=stop
    def __getitem__(self,index):
        if index<self.stop:
            return index            #식 조합해서 다른 숫자 나오게도 할수 있겟꾼
        else:
            raise IndexError
        
print(Counter(3)[0],Counter(3)[1],Counter(3)[2])
for i in Counter(3):
    print(i, end=" ")
    
A=Counter(3)
print(A[0],A[1],A[2])