pets=[{"name":"구름","age":5},{"name":"초코","age":3},{"name":"아지","age":21},{"name":"호랑이","age":8}]
for item in pets:
    # print(item["name"],str(item["age"])+"살")
    print(item.get("name"),str(item.get("age"))+"살")