from logics.battle import start_battle
from models.player import Player

DEBUG = True

while True:
    p1_name = input("Type name for player A:")
    p2_name = input("Type name for player B:")
    p1 = Player(p1_name)
    p2 = Player(p2_name)
    if DEBUG:
        print(p1.__dict__)
        print(p2.__dict__)
    start_battle(p1, p2)
