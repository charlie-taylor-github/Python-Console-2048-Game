import os

class Interface:
    def __init__(self):
        self._key_dir_map = {
            "w": "up",
            "a": "left",
            "s": "down",
            "d": "right"
        }
    
    def get_start_settings(self):
        os.system("clear")
        print(
        """
        Welcome to Python console 2048
        Enter a board size (1 to 8)
        """
        )
        failed = False
        while True:
            helper = "an integer from 1 to 8" if failed else ""
            size = input(helper + ":")
            if size.isdigit():
                return {
                    "board-size": int(size)
                }
            else:
                failed = True
            
    
    def display_board(self, board):
        os.system("clear")

        w = board.width
        row_divider = ("--------" * w) + "-"

        for row in board.contents:
            print(row_divider)
            print(self.__get_row_text([None] * w))
            print(self.__get_row_text(row))
            print(self.__get_row_text([None] * w))
        print(row_divider)
    
    def display_score(self, score):
        print(f"score: {str(score)}")
    
    def get_move_direction(self):
        failed = False
        while True:
            helper = "enter w, a, s or d" if failed else ""
            key = input(helper + ":")
            if key in self._key_dir_map:
                return self._key_dir_map[key]
            else:
                failed = True
    
    def display_gameover(self):
        print("Game Over!")
    
    def get_play_again(self):
        print("Play Again? (y/n)")
        failed = False
        while True:
            helper = "enter y or n" if failed else ""
            answer = input(helper + ":")
            if answer in ["y", "n"]:
                if answer == "n":
                    print("Thanks for playing!")
                return answer == "y"
            else:
                failed = True
    
    def __get_row_text(self, row):
        row_text = ""
        for space in row:
            row_text += "|"
            row_text += self.__get_space_text(space)
        row_text += "|"
        return row_text
    
    def __get_space_text(self, space):
        space_length = 7
        if not space:
            return " " * space_length
        
        value_length = len(str(space.value))
        spaces_left = space_length - value_length
        if spaces_left % 2 == 0:
            side_space = ' ' * int(spaces_left / 2)
            return f"{side_space}{str(space.value)}{side_space}"
        left_space = ' ' * int(spaces_left / 2)
        right_space = ' ' * (int(spaces_left / 2) + 1)
        return f"{left_space}{str(space.value)}{right_space}"
        