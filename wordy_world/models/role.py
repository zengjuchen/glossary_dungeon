# -*- coding: utf-8 -*-

"""
 This is player/monster module
"""
import time
import random
from models.base import Base
from models.skill import Skill

INIT_ATTR_RANGE = [5]*1 + [6]*2 + [7]*3 + [8]*4 + [9]*3 + [10]*2 + [11]*1
MAX_ATK = 10
MAX_ATK_SPEED = 10
MAX_HP_BASE = 10


class Role(Base):

    HP_FACTOR = 5
    CRITICAL_DAMAGE_FACTOR = 10

    def __init__(self, name, **kwargs):

        self.name = name
        self.attrs = random.choice(INIT_ATTR_RANGE)
        self.remain_attrs = self.attrs

        # BASIC ATTR ACQUISITION
        self.atk = random.choice(range(1, min([MAX_ATK, self.remain_attrs + 1 if self.remain_attrs > 2 else 2])))
        self.remain_attrs -= self.atk

        self.atk_speed = random.choice(range(1, min([MAX_ATK_SPEED, self.remain_attrs + 1 if self.remain_attrs > 2 else 2])))
        self.remain_attrs -= self.atk_speed

        self.hp = random.choice(range(1, min([MAX_HP_BASE, self.remain_attrs + 1 if self.remain_attrs > 2 else 2]))) * self.HP_FACTOR
        self.remain_attrs -= int(self.hp/self.HP_FACTOR)

        # ADVANCE ATTR ACQUISITION

        self.critical_damage_chance = random.choice(range(0, self.remain_attrs + 1 if self.remain_attrs > 0 else 1)) * self.CRITICAL_DAMAGE_FACTOR
        self.remain_attrs -= int(self.critical_damage_chance/self.HP_FACTOR)

        self.critical_damage_ratio = random.choice(range(0, self.remain_attrs + 1 if self.remain_attrs > 0 else 1))
        self.remain_attrs -= self.critical_damage_ratio
        self.dodge_chance = random.choice(range(0, self.remain_attrs + 1 if self.remain_attrs > 0 else 1)) * self.CRITICAL_DAMAGE_FACTOR
        self.remain_attrs -= int(self.dodge_chance/self.HP_FACTOR)

        # compute whose turn to attack
        self.atk_counter = 0

        self.skill_list = [Skill()]
