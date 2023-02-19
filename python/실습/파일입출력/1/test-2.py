import csv

def show_profit(data):
    name=data[0]    #종목
    purchae_price=int(data[1])   #매입가
    amount=int(data[2])     #수량
    target_price=int(data[3])   #목표가
    
    profit=(target_price-purchae_price)*amount  #수익금
    profit_ratio=(target_price/purchae_price-1)*100     #수익률
    
    print(f"{name} {profit} {profit_ratio:.2f}%")

file=open("./실습/파일입출력/1/mystock.csv","r")
reader=list(csv.reader(file))

for data in reader[1:]:
    show_profit(data)
file.close()