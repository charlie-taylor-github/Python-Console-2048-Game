from board import Board

class Game:
    def __init__(self, interface, width, on_game_over):
        self._board = Board(width)
        self._interface = interface
        self._on_game_over = on_game_over
    
    def start(self):
        while True:
            self._interface.display_board(self._board)
            self._interface.display_score(self._board.get_score())

            if self._board.get_is_gameover():
                self._interface.display_gameover()
                self._on_game_over()
                return
            
            direction = self._interface.get_move_direction()
            self._board.shift(direction)
