num=input("정수입력:")
# if(num%2==0):
#     print("짝수!")
# else:
#     print("홀수!")

# last_num=num[-1]
# last=int(last_num)
# if(last==0 or last==2 or last==4 or last==6 or last==8):
#     print("짝수!")
# else:
#     print("홀수!")

last=num[-1]
if(last in "02468"):
    print("짝수!")
else:
    print("홀수!")