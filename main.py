from interface import Interface
from game import Game

interface = Interface()

def setup_new_game():
    settings = interface.get_start_settings()
    game = Game(interface, settings["board-size"], on_game_over)
    game.start()

def on_game_over():
    play_again = interface.get_play_again()

    if play_again:
        setup_new_game()

setup_new_game()
