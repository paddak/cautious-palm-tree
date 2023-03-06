# for i in range(10):
#     print("1 * %d = %s"%(i,1*i))

# for i in range(10):
#     for j in range(10):
#         print("%d * %d = %d" %(i,j,i*j))
#     print("=======================")

m=int(input("몇단출력할까?"))
while(m<1 or m>9):
    m=int(input("1~9단까지만 가능"))

for n in range(10):
    print("%d * %d = %d" %(m,n,m*n))