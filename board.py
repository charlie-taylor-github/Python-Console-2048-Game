import random as rand
from piece import Piece
from board_shifter import BoardShifter

class Board:
    def __init__(self, width):
        self.width = width
        self.contents = None
        self.__initialize_board()
        self._shifter = BoardShifter(self)
    
    def shift(self, dir):
        self._shifter.shift(dir)
        self.__attempt_spawn_piece()
    
    def get_is_gameover(self):
        for i, row in enumerate(self.contents):
            if None in row:
                return False
            
            for j in range(self.width):
                if self.__get_pos_has_adjacent_piece({"row": i, "col": j}):
                    return False

        return True
    
    def get_score(self):
        score = 0
        for row in self.contents:
            for piece in row:
                if piece:
                    score += piece.value
        return score
    
    def __get_pos_has_adjacent_piece(self, pos):
        board = self.contents

        left_pos = {"row": pos["row"], "col": pos["col"] - 1}
        right_pos = {"row": pos["row"], "col": pos["col"] + 1}
        top_pos = {"row": pos["row"] - 1, "col": pos["col"]}
        bottom_pos = {"row": pos["row"] + 1, "col": pos["col"]}

        for pos2 in [left_pos, right_pos, top_pos, bottom_pos]:
            if self.__get_pieces_are_equal(pos, pos2):
                return True
        return False
    
    def __get_pieces_are_equal(self, pos1, pos2):
        board = self.contents
        for point in [pos1["row"], pos1["col"], pos2["row"], pos2["col"]]:
            if point < 0 or point > self.width - 1:
                return False

        piece1 = board[pos1["row"]][pos1["col"]]
        piece2 = board[pos2["row"]][pos2["col"]]

        if not (piece1 and piece2):
            return False
        
        return piece1.value == piece2.value

    def __initialize_board(self):
        self.contents = [
            [None] * self.width 
            for _ in range(self.width)
        ]

        for _ in range(2):
            self.__attempt_spawn_piece()
    
    def __attempt_spawn_piece(self):
        empty_positions = [
            {"row": i, "col": j}
            for i in range(len(self.contents)) 
            for j in range(len(self.contents[0])) 
            if self.contents[i][j] == None
        ]

        if empty_positions == []:
            return False

        pos = rand.choice(empty_positions)
        piece = self.__get_spawn_piece()
        self.contents[pos["row"]][pos["col"]] = piece

    def __get_spawn_piece(self):
        if rand.randint(0, 10) < 9:
            return Piece(2)
        return Piece(4)
