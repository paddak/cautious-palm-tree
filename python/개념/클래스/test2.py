class Monster:
    def __init__(self,health,attack,speed):
        self.health=health
        self.attack=attack
        self.speed=speed
    def decrease_health(self,num):
        self.health-=num
    def get_health(self):
        return self.health

Goblin=Monster(300,40,10)
Goblin.decrease_health(200)
print(Goblin.get_health())