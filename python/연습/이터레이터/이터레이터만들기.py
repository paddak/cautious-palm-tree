#이터레이터 만들기
class EX_Iterator:
    def __iter__(self):
        pass
    def __next__(self):
        pass

class Counter:
    def __init__(self,stop):            #객체 초기화
        self.current=0      #클래스 객체라 선언(안하면 밖에서 못씀)
        self.stop=stop
        
    def __iter__(self):
        return self         #현재 인스턴스 반환
    
    def __next__(self):
        if self.current<self.stop:
            r=self.current
            self.current +=1
            return r
        else:
            raise StopIteration     #예외발생

for i in Counter(3):
    print(i, end=" ")
    

#언패킹 하기
#Counter()결과를 변수여러개에 할당->이터레이터가 반복하는 횟수와 변수의 개수 같아야함
a,b,c=Counter(3)
print("\n")
print(a,b,c)

#map도 이터레이터
a,b,c=map(int,input().split())      #언패킹으로 변수 여러개에 값 할당

#반환값 _에 저장: 특정순서에 반환값 상ㅇ 안하고 무시하겠다
a,_,c,d=range(4)
print(a,_,c,d)