from logics.battle import battle
from models.role import Role
from logics.interface import execute


def start_game():
    current_interface = "interface.main"
    chosen_option = None
    print("\nWelcome to worldy world! May you enjoy your adventure!\n"
              "To quit game, type quit then press ENTER KEY.\n")

    while True:
        hints, current_interface = execute(current_interface, chosen_option)
        chosen_option = input(hints)
        if chosen_option in ['exit', 'EXIT', 'quit', 'Quit']:
            break


if __name__ == "__main__":
    start_game()
