import random

class Monster:
    max_num=1000
    def __init__(self,name,health,attack):
        self.name=name
        self.health=health
        self.attack=attack
        Monster.max_num-=1
    def move(self):
        print(f"[{self.name}]걷는다")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}]헤엄헤엄")

class Eagle(Monster):
    def __init__(self,name,health,attack):
        super().__init__(name,health,attack)
        self.skills=("불뿜기","꼬리치기","날개치기")

    def move(self):
        print(f"[{self.name}] 날다")
    
    def skill(self):
        print(f"{self.name} 스킬사용 {self.skills[random.randint(0,2)]}")

wolf=Wolf("울프",4000,30)
wolf.move()
print(wolf.max_num)

shark=Shark("상어",2000,300)
shark.move()
print(shark.max_num)

eagle=Eagle("독수리",40000,1)
eagle.move()
eagle.skill()