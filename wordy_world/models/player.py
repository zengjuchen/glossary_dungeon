# -*- coding: utf-8 -*-

"""
 This is player
"""
import random


ATK_RANGE = 10
ATK_INTERVAL_RANGE = 10
HP_RANGE = 100


class Player(object):

    def __init__(self, name):

        self.name = name
        self.atk = random.choice(range(ATK_RANGE))
        self.hp = random.choice(range(HP_RANGE))
        self.atk_interval = random.choice(range(ATK_INTERVAL_RANGE))
        # 用于计算轮到谁攻击的属性
        self.atk_counter = 0
