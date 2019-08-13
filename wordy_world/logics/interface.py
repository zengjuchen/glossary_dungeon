from logics import role, battle, bet

INVALID_INPUT_HINTS = "INVALID USER INPUT, input: {user_input}, interface-name: {interface}.\n\n"
ERROR_PROMPT = "{error}, This option is not valid now, please contact the developer to report the bug.\n Now we return back to main interface.\n"
BACK_COMMANDS = ["back", "BACK"]


def execute(interface_name, user_input=None):
    """
    execute actions based on input and interface, returns next interface_name

    :param user_input: str,
    :param interface_name: str,
    :return: (str, str)
    """
    interface_map = _parse_interface_name(interface_name)
    if interface_name not in interface_map:
        log = ERROR_PROMPT.format(error=interface_name)
        result = log, "main"
    else:
        result = interface_map[interface_name](user_input)
    return result


def _parse_interface_name(interface_name):
    """
    :param interface_name:
    :return: dict, Corresponding interface map
    """
    interface_parts = interface_name.split('.')
    if interface_name.startswith('bet'):
        return bet.INTERFACE_MAP
    return INTERFACE_MAP


def main(user_input):
    """

    :param user_input:  str
    :return:  (str, str)
    """
    options = {
        "1" : {'description': "Create roles for battle.", 'interface': ROLE_MAIN},
        "2" : {'description': "Start battle.", 'interface': BATTLE_MAIN},
        "3" : {'description': "Bet the game!", 'interface': BET_MAIN},
    }
    if user_input is None:
        log = "You have following options in current interface\n(type the number and press ENTER key to choose it):\n"
        for number, name_dict in options.items():
            log += "%s:  %s\n" % (number, name_dict['description'])
        return (log, 'interface.main')
    else:
        if user_input not in options.keys():
            log = INVALID_INPUT_HINTS.format(interface="interface.main", user_input=user_input)
            log += "You have following options in current interface(type the number and press ENTER key to choose it):\n"
            for number, name_dict in options.items():
                log += "%s:  %s\n" % (number, name_dict['description'])
            return (log, "interface.main")
        else:
            return (options[user_input]['description'], options[user_input]['interface'])


INTERFACE_MAIN = 'interface.main'
ROLE_MAIN = 'role'
BATTLE_MAIN = 'battle'
BET_MAIN = 'bet.main'


INTERFACE_MAP = {
    INTERFACE_MAIN: main,
    ROLE_MAIN: role.main,
    BATTLE_MAIN: battle.battle,
    BET_MAIN: bet.main,
}

