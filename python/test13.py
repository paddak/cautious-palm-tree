numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
count={}

for i in numbers:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1

print(count)