import time
import random
import settings
from utils.debug import debug_print

STANDARD_PAUSE = 1


def battle(player_list):
    if not player_list:
        player_list = settings.player_list
    player_list = [i for i in player_list if i.hp > 0]
    while True:
        if len(player_list) == 1:
            print("%s win the battle" % player_list[0].name)
            break

        initiator = min(player_list, key=lambda x: x.atk_counter)
        # TODO Can abstract to function later
        skill = random.choice(initiator.skill_list)
        # TODO choose_bearer and apply_action can combine
        bearer_list = [i for i in player_list if i != initiator]
        bearer = random.choice(bearer_list)

        #debug_print([initiator.name, bearer.name], tag="DEBUG INI-BEAR")
        logs = skill.orchestrate_actions(initiator, bearer)
        for log in logs:
            display_speed = getattr( settings, 'display_speed', 1)
            pause_time = STANDARD_PAUSE/initiator.atk_speed * display_speed
            time.sleep(pause_time)
            print(log)
        player_list = [i for i in player_list if i.hp > 0]
        #debug_print([i.name for i in player_list])
    return ("battle ends", "interface.main")

