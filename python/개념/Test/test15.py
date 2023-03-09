# def power(item):
#     return item*item

# def under(item):
#     return item<3

# arr=[1,2,3,4,5]

# output1=map(power,arr)
# print(list(output1))

# output2=filter(under,arr)
# print(list(output2))

# output3=filter(under,arr)
# print(list(output3))

#output4=filter(power,arr)
# print(list(arr))

power=lambda x:x*x
under=lambda x:x<3
arr=[1,2,3,4,5]

a=map(power,arr)
print(list(a))

b=filter(under,arr)
print(list(b))