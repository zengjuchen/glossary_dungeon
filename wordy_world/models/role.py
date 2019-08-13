# -*- coding: utf-8 -*-

"""
 This is player/monster module
"""
import time
import random
from models.base import Base
from models.skill import Skill

ATTR_RANGE_POOL = [5] * 1 + [6] * 2 + [7] * 3 + [8] * 4 + [9] * 3 + [10] * 2 + [11] * 1

INIT_ATTR_RANGES = {
   'hp': (1, 20),
   'atk': (1, 10),
   'atk_speed': (1, 10),
}

ATTR_FACTORS = {
   'hp': 5,
   'critical_hit_damage': 10,
}

class Role(Base):

    HP_FACTOR = 5
    CRITICAL_DAMAGE_FACTOR = 10
    INIT_ATTR_LIST = ['hp', 'atk', 'atk_speed', 'critical_hit_damage', 'critical_hit_chance']

    def __init__(self, name, **kwargs):
        super().__init__()

        self.name = name
        # compute whose turn to attack
        self.atk_counter = 0
        self.skill_list = [Skill()]

        self.init_attrs = self.remain_attrs = random.choice(ATTR_RANGE_POOL)
        for attr in self.INIT_ATTR_LIST:
            min_attr_val, max_attr_val = INIT_ATTR_RANGES.get(attr, (0, 9999))
            if self.remain_attrs <= min_attr_val:
                extra_attr_val = 0
            else:
                extra_attr_val = random.choice(range(min_attr_val, min([max_attr_val, self.remain_attrs])))
            self.remain_attrs -= extra_attr_val
            self[attr] = (min_attr_val + extra_attr_val) * ATTR_FACTORS.get(attr, 1)
