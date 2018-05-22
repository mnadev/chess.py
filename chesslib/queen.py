from chesslib import bishop
from chesslib import rook

class Queen:
    currPos = ""
    color = ""

    # a queen is basically a rook  and bishop together
    # no need to rewrite logic for this
    bishop = None
    rook = None

    def __init__(self, curr_pos, color):
        self.currPos = curr_pos
        self.color = color
        self.bishop = bishop.Bishop(curr_pos, color)
        self.rook = rook.Rook(curr_pos, color)

    def moves(self, board):
        moves = self.rook.moves(board) + self.bishop.moves(board)
        return moves

    def change_pos(self, new_pos):
        self.currPos = new_pos
        self.bishop.currPos = new_pos
        self.rook.currPos = new_pos

    def to_string(self):
        return "q" + str(self.color[0])
