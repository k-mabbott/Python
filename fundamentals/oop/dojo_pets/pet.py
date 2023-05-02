import ninja

class Pet: 
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):  # - increases the pets energy by 25
        print(f"Energy before sleep: {self.energy}")
        self.energy += 25
        print(f"{self.name}..zZzZzZ")
        print(f"Energy after sleep: {self.energy}")
        return self
    
    def eat(self):  # - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print(f"{self.name} loved the food Energy went up to: {self.energy} Health went up to {self.health}")
        return self
    
    def play(self):  # - increases the pet's health by 5
        self.health += 5
        return self
    
    def noise(self):  # - prints out the pet's sound
        print(f"{self.name} Barked!")
        return self

    def __repr__(self):
        return f"Name: {self.name} Type: {self.type} Tricks: {self.tricks} Health: {self.health} Energy: {self.energy} "


class Cat(Pet):
    def __init__(self, name, type,tricks, health, energy, couches_destroyed=0):
        super().__init__(name, type, tricks, health, energy)
        self.couches_destroyed = couches_destroyed

    def play(self):
        print(f"{self.name} destroyed a couch..")
        self.couches_destroyed += 1

    def __repr__(self):
        return f"Name {self.name} Type {self.type} Tricks {self.tricks} Health {self.health} Energy {self.energy} Couches destroyed: {self.couches_destroyed}"
    




# cedar = Pet('Cedar', 'Dog', ['laydown', 'sit', 'roll over'], 60, 50)
