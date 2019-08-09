from logics.battle import battle
from models.role import Role


DEBUG = True
player_list = []

while True:
    command = input("Type random name to add new player, type 'start' to start battle:")
    if command not in ["start", "'start'", '"start"']:
        player = Role(command)
        player_list.append(player)
    else:
        if DEBUG:
            for player in player_list:
                print(player.__dict__)

        battle(player_list)
        break
