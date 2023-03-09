ex=["A","B","C"]
# i=0
# for j in ex:
#     print("{}번째 요소는 {}".format(i,j))
#     i+=1

# for j in range(len(ex)):
#     print("{}번째 요소는 {}".format(j,ex[j]))

# for i, j in enumerate(ex):
#     print("{}번째 요소는 {}".format(i,j))

# ex1={"a":1,"b":2,"c":3}
# print("items():",ex1.items())

# ex3=[]
# for i in range(0,20,2):
#     ex3.append(i*i)
# print(ex3)

# ex4=[i*i for i in range(0,20,2)]
# print(ex4)

# a=[273]
# b=(273)
# c=(273,)
# print(type(a))
# print(type(b))
# print(type(c))

# ex5="a","b","c","d"
# print(type(ex5))

# a=(10,20)
# print(a)
# a=(30,40)
# print(a)

def test():
    return 10,20

a,b=test()
print(a)        #a=10
print(b)        #b=20