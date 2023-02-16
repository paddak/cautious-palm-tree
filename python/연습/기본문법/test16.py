import random


num=random.randint(1,20)

for i in range(4,-1,-1):
    a=int(input("기회가{}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:".format(i)))
    if(a==num):
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i))
        break
    elif(a!=num):
        if(a>num):
            print("Down")
        elif(a<num):
            print("Up")
        else:
            if(i==0):
                print("아쉽습니다 정답은 {}였습니다".format(i))
