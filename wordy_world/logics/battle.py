import time


def start_battle(p1, p2):
    while p1.hp > 0 and p2.hp > 0:
        attacker, defender = allocate_role(p1, p2)
        attacker.atk_counter += attacker.atk_interval
        defender.hp -= attacker.atk
        time.sleep(0.1)
        print("{attacker.name} attacks {defender.name}, deals {attacker.atk} damage, {defender.name} has {defender.hp} hp left".format(attacker=attacker, defender=defender))

        if defender.hp < 0:
            print("{defender.name} was defeated, {attacker.name} win".format(defender=defender, attacker=attacker))


def allocate_role(p1, p2):
    """
        决定谁是攻击者，谁是防御者
    """
    participants = [p1, p2]
    attacker = min(participants, key=lambda x: x.atk_counter)
    del participants[participants.index(attacker)]
    defender = participants[0]

    return attacker, defender
