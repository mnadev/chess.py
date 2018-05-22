class King:
    currPos = ""
    color = ""

    def __init__(self, curr_pos, color):
        self.currPos = curr_pos
        self.color = color

    def is_in_check(self, board):

        for i in range(0,8):

            for j in range(0,8):

                if not (board[i][j] is None):

                    if board[i][j].color != self.color:

                        list_moves = board[i][j].moves(board)

                        for m in list_moves:

                            if m == self.currPos:
                                return True

        return False


    def moves(self, board):
        moves = []

        x = ord(self.currPos[0])
        y = int(self.currPos[1])

        if y < 8:
            if board[y - 1 + 1][x - 97] is None:
                moves.append(chr(x) + str(y + 1))
            elif board[y - 1 + 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y + 1))

            if x < 104:
                if board[y - 1 + 1][x - 97 + 1] is None:
                    moves.append(chr(x + 1) + str(y + 1))
                elif board[y - 1 + 1][x - 97 + 1].color != self.color:
                    moves.append(chr(x + 1) + str(y + 1))

            if x > 97:
                if board[y - 1 + 1][x - 97 - 1] is None:
                    moves.append(chr(x - 1) + str(y + 1))
                elif board[y - 1 + 1][x - 97 - 1].color != self.color:
                    moves.append(chr(x - 1) + str(y + 1))

        if y > 1:
            if board[y - 1 - 1][x - 97] is None:
                moves.append(chr(x) + str(y - 1))
            elif board[y - 1 - 1][x - 97].color != self.color:
                moves.append(chr(x) + str(y - 1))

            if x < 104:
                if board[y - 1 - 1][x - 97 + 1] is None:
                    moves.append(chr(x + 1) + str(y - 1))
                elif board[y - 1 - 1][x - 97 + 1].color != self.color:
                    moves.append(chr(x + 1) + str(y - 1))

            if x > 97:
                if board[y - 1 - 1][x - 97 - 1] is None:
                    moves.append(chr(x - 1) + str(y - 1))
                elif board[y - 1 - 1][x - 97 - 1].color != self.color:
                    moves.append(chr(x - 1) + str(y - 1))

        if x < 104:
            if board[y - 1][x - 97 + 1] is None:
                moves.append(chr(x + 1) + str(y))
            elif board[y - 1][x - 97 + 1].color != self.color:
                moves.append(chr(x + 1) + str(y))

        if x > 97:
            if board[y - 1][x - 97 - 1] is None:
                moves.append(chr(x - 1) + str(y))
            elif board[y - 1][x - 97 - 1].color != self.color:
                moves.append(chr(x - 1) + str(y))

        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos

    def to_string(self):
        return "k" + str(self.color[0])
