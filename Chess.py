from chesslib.bishop import Bishop
from chesslib.rook import Rook
from chesslib.queen import Queen
from chesslib.king import King
from chesslib.pawn import Pawn
from chesslib.knight import Knight

board = [
    [Rook("a1","white"), Knight("b1","white"), Bishop("c1","white")
     , Queen("d1","white"), King("e1","white"), Bishop("f1","white")
     , Knight("g1","white"), Rook("h1","white")],
    [Pawn("a2","white"), Pawn("b2","white"), Pawn("c2","white")
     , Pawn("d2","white"), Pawn("e2","white"), Pawn("f2","white")
     , Pawn("g2","white"), Pawn("h2","white")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn("a7","black"), Pawn("b7","black"), Pawn("c7","black")
     , Pawn("d7","black"), Pawn("e7","black"), Pawn("f7","black")
     , Pawn("g7","black"), Pawn("h7","black")],
    [Rook("a8","black"), Knight("b8","black"), Bishop("c8","black")
     , Queen("d8","black"), King("e8","black"), Bishop("f8","black")
     , Knight("g8","black"), Rook("h8","black")]
]

board = [*zip(*board)]


def checkmateOccured():

    return False;


def check_move_validity(piece, curr_pos, new_pos):
    for m in piece.moves(curr_pos):
        if m == new_pos:
            return True;

    return False


def ask_user(player):

    ask_str = player + "\'s move"
    move = input(ask_str).strip()

    while move.strip().__len__() < 5:
        print("Wrong Format")
        move = input(ask_str).strip()

    return move


def print_board():

    print("a  b  c  d  e  f  g  h")

    for i in range(0,8):
        row = str(i + 1)
        for j in range(0,8):
            if board[i][j] is None:
                row += " " + ".."
            else:
                row += " " + board[i][j].to_string
        print(row)


def move_piece(curr_pos, new_pos):
    curr_piece = board[ord(curr_pos[0]) - 97 - 1][int(curr_pos[1]) - 1]
    board[ord(new_pos[0]) - 97 - 1][int(new_pos[1]) - 1] = curr_piece
    board[ord(curr_pos[0]) - 97 - 1][int(curr_pos[1]) - 1] = None


if __name__ == '__main__':

    whiteMove = True

    print_board()

    while not self.checkmateOccured():

        if whiteMove:
            move = ask_user("white")

        else:
            move = ask_user("black")

        curr_pos = move[:2]
        new_pos = move[3:5]

        if move.__len__() > 5:
            request = move[5:]
            if request == "resign":
                if whiteMove:
                    print("Black wins")
                else:
                    print("White wins")

        curr_piece = board[ord(curr_pos[0]) - 97 - 1][int(curr_pos[1]) - 1]

        while not check_move_validity(curr_piece, curr_pos, new_pos):
            if whiteMove:
                move = ask_user("white")
            else:
                move = ask_user("black")

            curr_pos = move[:2]
            new_pos = move[3:5]

            if move.__len__() > 5:
                request = move[5:]
                if request == "resign":
                    if whiteMove:
                        print("Black wins")
                    else:
                        print("White wins")

            curr_piece = board[ord(curr_pos[0]) - 97 - 1][int(curr_pos[1]) - 1]

        move_piece(curr_pos, new_pos)
        print_board()

        whiteMove = ~whiteMove
