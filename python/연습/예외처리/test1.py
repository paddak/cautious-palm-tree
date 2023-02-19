#원화,환율입력->달러

won=input("원화입력:")
dollar=input("환율입력:")

try:    #예외발생할수잇는코드
    print(int(won)/int(dollar))
except ValueError as e: #예외발생했을떄 실행되는 코드
    print("문자넣었네",e)
except ZeroDivisionError as e:
    print("0으로 나눴네",e)
else:   #예외발생안했을떄 나오는코드
    print("정상!")
finally: #항상실행코드
    print("예외 발생하든 안되는 실행됨")