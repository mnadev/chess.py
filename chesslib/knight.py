class Knight:
    currPos = ""
    color = ""

    def __init__(self, curr_pos, color):
        self.currPos = curr_pos
        self.color = color

    def moves(self, board):
        moves = []

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        if x < 104:
            if y < 7:
                if board[x - 97 + 1][y - 1 + 2] is None:
                    moves.append(chr(x + 1) + str(y + 2))
                elif board[x - 97 + 1][y - 1 + 2].color != self.color:
                    moves.append(chr(x + 1) + str(y + 2))

            if y > 2:
                if board[x - 97 + 1][y - 1 - 2] is None:
                    moves.append(chr(x + 1) + str(y - 2))
                elif board[x - 97 + 1][y - 1 - 2].color != self.color:
                    moves.append(chr(x + 1) + str(y - 2))

        if x > 97:
            if y < 7:
                if board[x - 97 - 1][y - 1 + 2] is None:
                    moves.append(chr(x - 1) + str(y + 2))
                elif board[x - 97 - 1][y - 1 + 2].color != self.color:
                    moves.append(chr(x - 1) + str(y + 2))

            if y > 2:
                if board[x - 97 - 1][y - 1 - 2] is None:
                    moves.append(chr(x - 1) + str(y - 2))
                elif board[x - 97 - 1][y - 1 - 2].color != self.color:
                    moves.append(chr(x - 1) + str(y - 2))

        if y < 7:
            if x < 103:
                if board[x - 97 + 2][y - 1 + 1] is None:
                    moves.append(chr(x + 2) + str(y + 1))
                elif board[x - 97 + 2][y - 1 + 1].color != self.color:
                    moves.append(chr(x + 2) + str(y + 1))

            if x > 98:
                if board[x - 97 - 2][y - 1 + 1] is None:
                    moves.append(chr(x - 2) + str(y + 1))
                elif board[x - 97 - 2][y - 1 + 1].color != self.color:
                    moves.append(chr(x - 2) + str(y + 1))

        if y > 1:
            if x < 103:
                if board[x - 97 + 2][y - 1 - 1] is None:
                    moves.append(chr(x + 2) + str(y - 1))
                elif board[x - 97 + 2][y - 1 - 1].color != self.color:
                    moves.append(chr(x + 2) + str(y - 1))

            if x > 98:
                if board[x - 97 - 2][y - 1 - 1] is None:
                    moves.append(chr(x - 2) + str(y - 1))
                elif board[x - 97 - 2][y - 1 - 1].color != self.color:
                    moves.append(chr(x - 2) + str(y - 1))

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos

    def to_string(self):
        return "n" + self.color[0]
