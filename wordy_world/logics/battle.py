import time

STANDARD_PAUSE = 1
LAST_ATTACKER = None


def start_battle(p1, p2, display_speed=1):
    while p1.hp > 0 and p2.hp > 0:
        attacker, defender = allocate_role(p1, p2)
        defender.atk_counter += defender.atk_speed
        defender.hp -= attacker.atk
        rendering(attacker, defender, display_speed=display_speed)


def allocate_role(p1, p2):
    """
        决定谁是攻击者，谁是防御者
    """
    participants = [p1, p2]
    attacker = max(participants, key=lambda x: x.atk_counter)
    del participants[participants.index(attacker)]
    defender = participants[0]

    return attacker, defender


def rendering(attacker, defender, display_speed):
    global LAST_ATTACKER
    if LAST_ATTACKER != attacker:
        print('')
        LAST_ATTACKER = attacker
    animation_pause(attacker.atk_speed, display_speed)
    print("{attacker.name} attacks {defender.name}, deals {attacker.atk} damage, {defender.name} has {defender.hp} hp left".format(attacker=attacker, defender=defender))

    if defender.hp < 0:
        print("{defender.name} was defeated, {attacker.name} win".format(defender=defender, attacker=attacker))


def animation_pause(atk_speed, display_speed):
    """
        decide How many seconds to pause between each round
    """
    pause_time = STANDARD_PAUSE/atk_speed * display_speed
    time.sleep(pause_time)
