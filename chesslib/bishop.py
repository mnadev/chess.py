class Bishop:
    currPos = ""
    color = ""

    def __init__(self,currPos, color):
        self.currPos = currPos
        self.color = color

    def moves(self, board):
        moves = []

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while x > 97 and y > 1:
            x = x - 1
            y = y - 1
            if board[y - 1][x - 97] is None:
                moves.append(chr(x) + str(y))
            elif board[y - 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while x > 97 and y < 8:
            x = x - 1
            y = y + 1
            if board[y - 1][x - 97] is None:
                moves.append(chr(x) + str(y))
            elif board[y - 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        while x < 104 and y > 1:
            x = x + 1
            y = y - 1
            if board[y - 1][x - 97] is None:
                moves.append(chr(x) + str(y))
            elif board[y - 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        while x < 104 and y < 8:
            x = x + 1
            y = y + 1
            if board[y - 1][x - 97] is None:
                moves.append(chr(x) + str(y))
            elif board[y - 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y))
                break
            else:
                break

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos

    def to_string(self):
        return "b" + str(self.color[0])
