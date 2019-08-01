# -*- coding: utf-8 -*-

"""
 This is player
"""
import random

INIT_ATTR_RANGE = [5]*1 + [6]*2 + [7]*3 + [8]*4 + [9]*3 + [10]*2 + [11]*1
MAX_ATK = 10
MAX_ATK_SPEED = 10
MAX_HP_BASE = 10


class Player(object):

    def __init__(self, name):

        self.name = name
        self.attrs = random.choice(INIT_ATTR_RANGE)
        self.atk = random.choice(range(1, min([MAX_ATK, self.attrs + 1 if self.attrs > 2 else 2])))
        self.atk_speed = random.choice(range(1, min([MAX_ATK_SPEED, self.attrs + 1 if self.attrs > 2 else 2])))
        self.hp = random.choice(range(1, min([MAX_HP_BASE, self.attrs + 1 if self.attrs > 2 else 2]))) * 10
        # compute whose turn to attack
        self.atk_counter = 0
