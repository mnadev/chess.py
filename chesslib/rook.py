class Rook:
    currPos = ""
    color = ""
    firstMove = True

    def __init__(self, curr_pos, color):
        self.currPos = curr_pos
        self.color = color
        self.firstMove = True

    def moves(self, board):
        moves = []

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while x > 97:
            x = x - 1
            if board[x - 97][y - 1] is None:
                moves.append(chr(x) + str(y))
            elif board[x - 97][y - 1].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while x < 104:
            x = x + 1
            if board[x - 97][y - 1] is None:
                moves.append(chr(x) + str(y))
            elif board[x - 97][y - 1].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while y < 8:
            y = y + 1
            if board[x - 97][y - 1] is None:
                moves.append(chr(x) + str(y))
            elif board[x - 97][y - 1].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while y > 1:
            y = y - 1
            if board[x - 97][y - 1] is None:
                moves.append(chr(x) + str(y))
            elif board[x - 97][y - 1].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos
        self.firstMove = False

    def to_string(self):
        return "r" + self.color[0]
