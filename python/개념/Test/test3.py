# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark >= 60: 
#         print("%d번 학생은 합격입니다." % number)
#     else: 
#         print("%d번 학생은 불합격입니다." % number)

# i=1,2,3,4,5
# for ia in i:
#     if ia>3:
#         print("성공!")
#     else:
#         print("실패!")

# print(list(range(0,10,3)))

# signal='blue','yellow','red'
# for x in range(len(signal)):
#     print(x,signal[x],len(signal[x]))

# for x in signal:
#     print(x)

# nest=[[1,2,3],[4,5,6],[7,8,9]]
# for x in range(3):
#     for y in range(3):
#         print(nest[x][y])

# squares=[]
# for i in range(10):
#     squares.append(i**2)
# print(squares)

nsquare=[y**2 for y in range(10)]
print(nsquare)
