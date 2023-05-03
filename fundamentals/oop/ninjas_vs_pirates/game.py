from ninja import Ninja
from pirate import Pirate
import random


pirate1 = Pirate()
ninja1 = Ninja()

print('Welcome to Ninjas vs Pirates!!')
player_choice = input('Which character do you want to play as? /n 1 for ninja or 2 for pirate \n')
if player_choice == '1':
    player = ninja1
    opponent = pirate1
elif player_choice == '2':
    player = pirate1
    opponent = ninja1
player.name = input("What is his name? \n")

while player.health >= 0 and opponent.health >= 0:
    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input("Choose an action \n 1)Attack \n 2)Use Special \n 3)Use Buff \n >>>")
    print('\n')
    if response == '1':
        player.attack(opponent)
    elif response == '2':
        player.use_special(opponent)
    else:
        player.use_buff()

    print("\n--opponents turn!--\n")

    opponent_move = random.randint(1,3)
    if opponent_move == 1:
        opponent.attack(player)
    elif opponent_move == 2:
        opponent.use_special(player)
    else:
        opponent.use_buff()

    print('\n')

if opponent.health < 0 and player.health < 0:
    print("Wow a tie!!")
elif opponent.health < 0:
    print("Congrats you win!")
elif player.health < 0:
    print("Try again you lost!")
