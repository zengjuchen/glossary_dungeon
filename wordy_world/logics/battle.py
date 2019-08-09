import time
import random
from utils.debug import debug_print

STANDARD_PAUSE = 1
LAST_ATTACKER = None


def battle(player_list):
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
            animation_pause(initiator.atk_speed, log)
        player_list = [i for i in player_list if i.hp > 0]
        #debug_print([i.name for i in player_list])


def animation_pause(atk_speed, log, display_speed=1):
    """
        decide How many seconds to pause between each round
    """
    pause_time = STANDARD_PAUSE/atk_speed * display_speed
    time.sleep(pause_time)
    print(log)
