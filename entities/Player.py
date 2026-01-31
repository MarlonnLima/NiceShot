class Player:
    def __init__(self, name, health = 10):
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    def recover_health(self, amount):
        self.health += amount
        if self.health >= 10:
            self.health = 10

    def is_alive(self):
        return self.health > 0