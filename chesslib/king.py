class King:
    currPos = ""
    color = ""

    def __init__(self, curr_pos, color):
        self.currPos = curr_pos
        self.color = color

    def moves(self, board):
        moves = []

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        if y < 8:
            if board[x - 97][y - 1 + 1] is None:
                moves.append(chr(x) + str(y + 1))
            elif board[x - 97][y - 1 + 1].color != self.color:
                moves.append(chr(x) + str(y + 1))

            if x < 104:
                if board[x - 97 + 1][y - 1 + 1] is None:
                    moves.append(chr(x + 1) + str(y + 1))
                elif board[x - 97 + 1][y - 1 + 1].color != self.color:
                    moves.append(chr(x + 1) + str(y + 1))

            if x > 97:
                if board[x - 97 - 1][y - 1 + 1] is None:
                    moves.append(chr(x - 1) + str(y + 1))
                elif board[x - 97 - 1][y - 1 + 1].color != self.color:
                    moves.append(chr(x - 1) + str(y + 1))

        if y > 1:
            if board[x - 97][y - 1 - 1] is None:
                moves.append(chr(x) + str(y - 1))
            elif board[x - 97][y - 1 - 1].color != self.color:
                moves.append(chr(x) + str(y - 1))

            if x < 104:
                if board[x - 97 + 1][y - 1 - 1] is None:
                    moves.append(chr(x + 1) + str(y - 1))
                elif board[x - 97 + 1][y - 1 - 1].color != self.color:
                    moves.append(chr(x + 1) + str(y - 1))

            if x > 97:
                if board[x - 97 - 1][y - 1 - 1] is None:
                    moves.append(chr(x - 1) + str(y - 1))
                elif board[x - 97 - 1][y - 1 - 1].color != self.color:
                    moves.append(chr(x - 1) + str(y - 1))

        if x < 104:
            if board[x - 97 + 1][y - 1] is None:
                moves.append(chr(x + 1) + str(y))
            elif board[x - 97 + 1][y - 1].color != self.color:
                moves.append(chr(x + 1) + str(y))

        if x > 97:
            if board[x - 97 - 1][y - 1] is None:
                moves.append(chr(x - 1) + str(y))
            elif board[x - 97 - 1][y - 1].color != self.color:
                moves.append(chr(x - 1) + str(y))

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos

    def to_string(self):
        return "k" + self.color[0]
