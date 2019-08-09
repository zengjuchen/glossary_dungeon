# -*- coding: utf-8 -*-
from models.base import Base
"""
"""

class Skill(Base):
    TARGET = {
        'self': 0,
        'ally': 1,
        'enemey': 2,
        'self+ally': 3,
        'self+enemy': 4,
        'self+ally+enemy': 5,
    }

    def __init__(self, **kwargs):
        self.action_list = []
        for k, v in kwargs:
            self.__dict__[k] = v

    # TODO
    def orchestrate_actions(self, initiater, target):
        action = Action(initiater=initiater, target=target, value=initiater.atk)
        action_logs = action.apply()
        return action_logs

class Action(Base):

    BASIC_OPERATORS = ["+=", "-=", '%=', "*="]

    NORMAL_TYPE = 0

    def __init__(self, **kwargs):
        self.initiater = None
        self.target = None
        self.type = self.NORMAL_TYPE
        self.attr = 'hp'
        self.operator = '-='
        self.value = 1
        self.execute_timing = 0  # 0 means execute it immediately
        self.logs = []
        self.execute_count = 0

        for k, v in kwargs.items():
            self.__dict__[k] = v
        super().__init__()

    def apply(self):
        if not self.initiater or not self.target or self.target.hp <= 0:
            return
        if self.type == self.NORMAL_TYPE and self.execute_count >= 1:
            return
        if self.operator in self.BASIC_OPERATORS:
            exec("self.target.{attr} {operator} {value}".format(attr=self.attr, operator=self.operator, value=self.value))
            self.initiater.atk_counter += 1/self.initiater.atk_speed
        log = "{initiater.name} attacks {target.name}, deals {initiater.atk} damage, {target.name} has {target.hp} hp left".format(initiater=self.initiater, target=self.target)
        self.logs.append(log)
        self.execute_count += 1
        if self.target.hp <= 0:
            self.logs.append("%s died" % self.target.name)

        return self.logs
