players = [
    {
	"name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Jason Tatum", 
	"age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
    },
    {
	"name": "Kyrie Irving", 
	"age":32,
    "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Damian Lillard", 
	"age":33,
    "position": "Point Guard", 
	"team": "Portland Trailblazers"
    },
    {
	"name": "Joel Embiid", 
	"age":32,
    "position": "Power Foward", 
	"team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]
mine = {
    "name": "Kyle",
    "age": 30,
    "position": "Bad",
    "team": "None"
    }


class Player:

    all_players = []

    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']
        Player.all_players.append(self)

    def __repr__(self):
        return (f"Player: {self.name} Age: {self.age} Position: {self.position} Team: {self.team}")
        

    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for player in team_list:
            new_list.append(Player(player))
            
        return new_list

# team1 = []
# for i in range(1, len(players)):
#     team1.append(Player(players[i])) 
team1 = Player.get_team(players)

me = Player(mine)

print(team1)
print(Player.all_players)








# player_kevin = Player(players[0])
# player_jason = Player(players[1])
# player_kyrie = Player(players[2])
# player_damian = Player(players[3])
# player_joel = Player(players[4])
# player_demar = Player(players[5])

# new_team = []

# new_team.append(player_kevin)
# new_team.append(player_jason)
# new_team.append(player_kyrie)
# new_team.append(player_damian)
# new_team.append(player_joel)
# new_team.append(player_demar)

# team1 = Player.get_team(new_team)
# print(team1)

