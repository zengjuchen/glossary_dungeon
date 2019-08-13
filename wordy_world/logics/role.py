import settings
from models.role import Role
from logics.battle import battle
DEBUG = True


def main(user_input):
    player_list = []

    while True:
        command = input("Type random name to add new player, type 'OK' to finish role creation:")
        if command not in ["ok", "OK", 'exit', 'quit']:
            exists_local_role_names = [i.name for i in player_list]
            exists_global_role_names = [i.name for i in getattr(settings, 'player_list', [])]
            if command in exists_local_role_names or command in exists_global_role_names:
                print("Role name already exists, please type another name.")
                continue
            player = Role(command)
            player_list.append(player)
        else:
            if DEBUG:
                for player in player_list:
                    print(player.__dict__)
            if not getattr(settings, 'player_list', None):
                settings.player_list = player_list
            else:
                settings.player_list.extend(player_list)
            break
    return ('Role creation Finished.', 'interface.main')
