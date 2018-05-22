from chesslib.bishop import Bishop
from chesslib.rook import Rook
from chesslib.queen import Queen
from chesslib.king import King
from chesslib.pawn import Pawn
from chesslib.knight import Knight

kW = King("e1","white")
kB = King("e8","black")
board = [
    [Rook("a1","white"), Knight("b1","white"), Bishop("c1","white")
     , Queen("d1","white"), kW, Bishop("f1","white")
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
     , Queen("d8","black"), kB, Bishop("f8","black")
     , Knight("g8","black"), Rook("h8","black")]
]


def checkmate_occured(white_move):

    if white_move:
        color = "black"
        curr_king = kB
    else:
        color = "white"
        curr_king = kW

    for i in range(0,8):

        for j in range(0,8):

            if not (board[i][j] is None):

                if not board[i][j].color == color:

                    list_moves = board[i][j].moves(board)
                    curr = board[i][j].currPos

                    for m in list_moves:

                        old_piece = board[int(m[1]) - 1][ord(m[0]) - 97]
                        move_piece(curr, m)

                        if not curr_king.is_in_check(board):
                            move_piece(m, curr)
                            board[int(m[1]) - 1][ord(m[0]) - 97] = old_piece
                            return False

                        move_piece(m, curr)
                        board[int(m[1]) - 1][ord(m[0]) - 97] = old_piece

    return True


def check_move_validity(piece, new):
    for m in piece.moves(board):
        if m == new:
            return True;

    return False


def ask_user(player):

    ask_str = "\n" + player + "\'s move:"
    inp = input(ask_str).strip()

    while inp.strip().__len__() < 5:
        print("Wrong Format")
        inp = input(ask_str).strip()

    return inp


def print_board():

    print("   a  b  c  d  e  f  g  h")

    for i in range(0,8):
        row = str(i + 1)
        for j in range(0,8):
            if board[i][j] is None:
                row += " " + ".."
            else:
                row += " " + board[i][j].to_string()
        print(row)


def move_piece(curr, new):
    piece = board[int(curr[1]) - 1][ord(curr[0]) - 97]
    board[int(new[1]) - 1][ord(new[0]) - 97] = piece
    board[int(curr[1]) - 1][ord(curr[0]) - 97] = None


if __name__ == '__main__':

    whiteMove = True
    resign = False

    print_board()

    while not checkmate_occured(whiteMove) or resign:

        if whiteMove:
            move = ask_user("white")

        else:
            move = ask_user("black")

        curr_pos = move[:2]
        new_pos = move[3:5]

        if move.__len__() > 5:
            request = move[5:].strip()
            if request == "resign":
                resign = True
                if whiteMove:
                    print("Black wins")
                    break
                else:
                    print("White wins")
                    break

        curr_piece = board[int(curr_pos[1]) - 1][ord(curr_pos[0]) - 97]

        while not check_move_validity(curr_piece, new_pos):
            if whiteMove:
                move = ask_user("white")
            else:
                move = ask_user("black")

            curr_pos = move[:2]
            new_pos = move[3:5]

            if move.__len__() > 5:
                request = move[5:].strip()
                if request == "resign":
                    resign = True
                    if whiteMove:
                        print("Black wins")
                        break
                    else:
                        print("White wins")
                        break

            curr_piece = board[int(curr_pos[1]) - 1][ord(curr_pos[0]) - 97]

        move_piece(curr_pos, new_pos)
        print_board()

        whiteMove = not whiteMove
