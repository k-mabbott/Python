import pet
from ninja import Ninja


cedar = pet.Pet('Cedar', 'Dog', ['laydown', 'sit', 'roll over'], 60, 50)
me = Ninja("Kyle", "Mabbott", "yes", "cedar's", cedar )
philo = pet.Cat('Philo', 'Cat', 'none', 60, 100)


print(cedar)
me.bathe().walk().feed().walk()
cedar.sleep().eat().play().noise()
print(cedar)
me.feed()
print(philo)