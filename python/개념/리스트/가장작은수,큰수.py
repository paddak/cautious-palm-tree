#제일작은수
a=[124,2356,2463,32,35,3]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)

#제일큰수
largest=a[0]
for i in a:
    if i>largest:
        largest=1
print(largest)

#이래도 되는데 그냥 정렬해서 하면되겠네
#근데 min,max도 있다
print(min(a))
print(max(a))

#요소합계
x=0
for i in a:
    x+=i
print(x)
#sum쓰자
sum(a)