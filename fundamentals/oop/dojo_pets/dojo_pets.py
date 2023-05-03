import pet
# from ninja import Ninja
import ninja 

ninja.Ninja()

cedar = pet.Pet('Cedar', 'Dog', ['laydown', 'sit', 'roll over'], 60, 50)
me = ninja.Ninja("Kyle", "Mabbott", "yes", "cedar's", cedar )
philo = pet.Cat('Philo', 'Cat', 'none', 60, 100)


print(cedar)
me.bathe().walk().feed().walk()
cedar.sleep().eat().play().noise()
print(cedar)
me.feed()
print(philo)

