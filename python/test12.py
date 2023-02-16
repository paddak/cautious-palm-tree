numbers=[1,2,3,4,5,6,7,8,9]

for number in numbers:
    if(numbers[number-1]%2==0):
        numbers[number-1]=numbers[number-1]**2

print(numbers)
