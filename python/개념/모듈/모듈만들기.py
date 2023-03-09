import pay_module

#변수사용
print(pay_module.version)

#함수사용
pay_module.printAuthor()

#클래스사용
pay_info=pay_module.Pay("A102030",1300,"2023-92-15")
print(pay_info.get_pay_info())

print(pay_module.__name__) 