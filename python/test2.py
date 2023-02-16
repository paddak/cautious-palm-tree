color=''
while(color!="blue" and color!="red"):
    color=input("무슨색?")
    if(color=="blue"):
        print("파란불이네 건너자")
    elif(color=="red"):
        print("빨간불이네 다음에 건너자")
    else:
        print("다시쓸래?")

print("종료!")