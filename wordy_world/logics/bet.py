import settings
from logics import interface

CUR_INTERFACE_NAME = "bet.main"


def main(user_input):
    if user_input in interface.BACK_COMMANDS:
        return ("Back to upper interface", interface.INTERFACE_MAIN)
    options = {
        "1" : {'description': "show available roles", 'interface': SHOW_BET_INFO},
        "2" : {'description': "Bet on role.", 'interface': PLACE_BET},
        "3" : {'description': "Show bet result.", 'interface': SHOW_BET_RESULT},
    }
    if user_input is None:
        log = "You have following options in current interface\n(type the number and press ENTER key to choose it):\n"
        for number, name_dict in options.items():
            log += "%s:  %s\n" % (number, name_dict['description'])
        return (log, 'bet.main')
    else:
        if user_input not in options.keys():
            log = "You have following options in current interface(type the number and press ENTER key to choose it):\n"
            for number, name_dict in options.items():
                log += "%s:  %s\n" % (number, name_dict['description'])
            return (log, "bet.main")
        else:
            return (options[user_input]['description'], options[user_input]['interface'])


def show_bet_info(user_input):
    _calc_odds(settings.player_list)
    for player in [i for i in settings.player_list if i.hp > 0]:
        print("PLAYER INFO: ")
        print("name: ", player['name'])
        for attr_name in player.INIT_ATTR_LIST:
            print(attr_name, ":", player[attr_name])
        print("PLAYER BET ODDS: ", settings.bet_record[player]['odds'], '\n')
    return ("Bet odds showed, pree ENTER to continue:", interface.BET_MAIN)


def show_bet_result(user_input):
    for role, role_bet_record in settings.bet_record.items():
        is_winner = role.is_winner
        if role_bet_record.get('record'):
            for player_name, bet_num, odds in role_bet_record['record']:
                if is_winner:
                    print("{player_name} wins {money} as {role.name} is winner".format(player_name=player_name, money=bet_num*odds, role=role) )
                if is_winner == False:
                    print("{player_name} lose {money} as {role.name} lose the battle.".format(player_name=player_name, money=bet_num, role=role) )
    return ("Bet results showed, pree ENTER to continue:", interface.BET_MAIN)


def place_bet(user_input):
    if user_input in interface.BACK_COMMANDS:
        return ("Back to upper interface", BET_MAIN)

    player_name = input('Please type your name.')
    role_name = input("Please type the role name you'd like to bet on.")
    role_lsit = [i for i in settings.player_list if i.name == role_name]
    if not role_lsit or role_lsit[0].hp <= 0:
        return ("Invalid role name, type another role name:", PLACE_BET)
    role = role_lsit[0]
    odds = settings.bet_record[role]['odds']
    print("PLAYER INFO: ", role.__dict__)
    print("PLAYER BET ODDS: ", odds, '\n')
    bet_num = int(input("Please type the number you'd like to bet"))

    if role in settings.bet_record:
        settings.bet_record[role]['record'].append((player_name, bet_num, odds))
    else:
        settings.bet_record[role]['record'] = [(player_name, bet_num, settings.bet_record[role]['odds'])]
    return ("Bet placed successfully, pree ENTER to continue:", interface.BET_MAIN)


def _calc_odds(player_list):
    profit_rate = 0.15
    valid_players = [i for i in player_list if i.hp > 0]
    all_attrs = sum([i.init_attrs for i in valid_players])
    for player in valid_players:
        odds = ((1 - player.init_attrs / all_attrs) / (player.init_attrs / all_attrs)) * (1 - profit_rate)
        if player not in settings.bet_record:
            settings.bet_record[player] = {'odds': odds, 'record': []}
        else:
            settings.bet_record[player]['odds'] = odds


BET_MAIN = 'bet.main'
PLACE_BET = 'bet.place_bet'
SHOW_BET_INFO = 'bet.show_bet_info'
SHOW_BET_RESULT = 'bet.show_bet_result'

INTERFACE_MAP = {
    PLACE_BET: place_bet,
    SHOW_BET_INFO: show_bet_info,
    SHOW_BET_RESULT: show_bet_result,
    BET_MAIN: main,
}
