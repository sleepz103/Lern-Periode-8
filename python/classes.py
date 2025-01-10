class Character:
    def __init__(self, health , damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def run(self):
        self.speed *= 2
    def take_damage(self, damage):
        self.health -= damage

warrior = Character(100, 10, 10)