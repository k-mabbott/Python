import random

class Fighter:

    def __init__(self):
        self.health = 80
        self.defense = 5
        self.strength = 10
        self.agility = 1

    def attack(self, target):
        target.defense(self.strength)
        print(f"{self.name} attacked {target.name} their health is now {target.health}")

    def defense(self, amount):
        chance = random.randint(10 - self.agility)
        if chance < 2:
            print(f"{self.name} dodged the attack")
        else:
            damage = amount - self.defense 
            self.health -= damage
            print(f"{self.name} got attacked for {damage} points health left is {self.health}")

    def use_special():
        pass

    def use_buff():
        pass






    # chance = random.randint(10 - target.agility)
    # if chance > 3: