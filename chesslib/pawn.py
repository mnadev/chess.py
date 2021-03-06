class Pawn:

    # need to know color and current position of the piece
    currPos = ""
    color = ""

    # since this is a pawn we want to know if its a first move to let it move two spaces
    firstMove = True

    def __init__(self, currPos, color):
        self.currPos = currPos
        self.color = color
        self.firstMove = True

    def moves(self, board):
        moves = []

        # if white the pawn moves up otherwise it moves down
        if self.color == "white":

            x = ord(self.currPos[0])
            y = int(self.currPos[1])

            if y < 8:

                if board[(y - 1 + 1)][(x - 97)] is None:
                    moves.append(chr(x) + str(y + 1))
                elif board[y - 1 + 1][x - 97].color != self.color:
                    moves.append(chr(x) + str(y + 1))

                if x > 97:
                    if not board[y - 1 + 1][x - 97 - 1] is None:
                        if board[y - 1 + 1][x - 97 - 1].color != self.color:
                            moves.append(chr(x - 1) + str(y + 1))

                if x < 104:
                    if not board[y - 1 + 1][x - 97 + 1] is None:
                        if board[y - 1 + 1][x - 97 + 1].color != self.color:
                            moves.append(chr(x + 1) + str(y + 1))

            if self.firstMove:
                if board[y - 1 + 2][x - 97] is None:
                    moves.append(chr(x) + str(y + 2))
                elif board[y - 1 + 2][x - 97].color != self.color:
                    moves.append(chr(x) + str(y + 2))
        else:

            x = ord(self.currPos[0])
            y = int(self.currPos[1])

            if y > 1:
                if board[y - 1 - 1][x - 97] is None:
                    moves.append(chr(x) + str(y - 1))
                elif board[y - 1 - 1][x - 97].color != self.color:
                    moves.append(chr(x) + str(y - 1))

                if x < 104:
                    if not board[y - 1 - 1][x - 97 + 1] is None:
                        if board[y - 1 - 1][x - 97 + 1].color != self.color:
                            moves.append(chr(x + 1) + str(y - 1))

                if x > 97:
                    if not board[y - 1 - 1][x - 97 - 1] is None:
                        if board[y - 1 - 1][x - 97 - 1].color != self.color:
                            moves.append(chr(x - 1) + str(y - 1))

            if self.firstMove:
                if board[y - 1 - 2][x - 97] is None:
                    moves.append(chr(x) + str(y - 2))
                elif board[y - 1 - 2][x - 97].color != self.color:
                    moves.append(chr(x) + str(y - 2))

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos
        self.firstMove = False

    def to_string(self):
        return "p" + str(self.color[0])
