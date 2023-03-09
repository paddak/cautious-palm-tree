numbers=[273,103,5,32,65,9,72,800,99]

for i in numbers:
    if(i%2==0):
        print("{}는 짝수입니다".format(i))
    else:
        print("{}는 홀수입니다".format(i))

for i in numbers:
    if(i>=100):
        print("100이상의 수는",i)

for i in numbers:
    print(i,"는",len(str(i)),"자릿수입니다")