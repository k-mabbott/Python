
import random
from fighter import Fighter

class Pirate(Fighter):
    def __init__(self):
        super().__init__()
        self.name = 'Pirate'
        self.defense += 2
        self.strength += 2
        self.special = 'Parlay!'
        self.buff = 'Cure Scurvy'
    
    def use_special(self, target):
        print(f"{self.name} used {self.special} and shot at {target.name}!")
        crit_chance = random.randint(1, 5)
        target.defend(self.strength + crit_chance)
    
    def use_buff(self):
        print(f"{self.name} used {self.buff} and ate a bunch of oranges!")

        self.health += 5
        print(f"{self.name}'s health is now {self.health}")

