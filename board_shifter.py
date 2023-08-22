class BoardShifter:
    def __init__(self, board):
        self._board = board
    
    def shift(self, dir):
        b = self._board.contents
        rows = list(range(0, self._board.width))
        cols = list(range(0, self._board.width))
        if dir == "down":
            rows = rows[::-1]
        if dir == "right":
            cols = cols[::-1]
        for row in rows:
            for col in cols:
                space = b[row][col]
                if space:
                    pos = { "row": row, "col": col }
                    self.__shift_space(pos, dir)
    
    def __shift_space(self, pos, dir):
        shifted_pos, merged = self.__get_shifted_pos(pos, dir)
        piece = self.__get_space(pos)
        if merged:
            piece.value = piece.value * 2
        self._board.contents[pos["row"]][pos["col"]] = None
        self._board.contents[shifted_pos["row"]][shifted_pos["col"]] = piece
    
    def __get_shifted_pos(self, pos, dir):
        piece = self. __get_space(pos)
        while True:
            next_pos = self.__get_next_pos(pos, dir)
            if not self.__get_pos_in_bounds(next_pos):
                return pos, False
            next_space = self.__get_space(next_pos)
            if next_space:
                if next_space.value == piece.value:
                    return next_pos, True
                else:
                    return pos, False
            pos = next_pos    
    
    def __get_space(self, pos):
        row = self._board.contents[pos["row"]]
        return row[pos["col"]]
    
    def __get_pos_in_bounds(self, pos):
        r, c = pos["row"], pos["col"]
        w = self._board.width
        if r < 0 or r >= w:
            return False
        if c < 0 or c >= w:
            return False
        return True
    
    def __get_next_pos(self, pos, dir):
        if dir == "down":
            return {"row": pos["row"] + 1, "col": pos["col"]}
        if dir == "up":
            return {"row": pos["row"] - 1, "col": pos["col"]}
        if dir == "left":
            return {"row": pos["row"], "col": pos["col"] - 1}
        if dir == "right":
            return {"row": pos["row"], "col": pos["col"] + 1}
        return pos
