#coding=UTF-8
#In this chapter, we used the dictionary value
#{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
#to represent a chess board. Write a function named isValidChessBoard()
#that takes a dictionary argument and returns True or False depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white king.
#Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
#must be on a valid space from '1a' to '8h'; that is, a piece can?t be on space '9z'.
#The piece names begin with either a 'w' or 'b' to represent white or black,
#followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chess board.

chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(dictionary):

    white_pieces = [item for item in dictionary.values() if item[0] == 'w']
    black_pieces = [item for item in dictionary.values() if item[0] == 'b']

    if len(white_pieces) + len(black_pieces) > 32:
        print("Too many pieces on the board.")

    for place, figure in dictionary.items():
        if len(place) > 2 or int(place[0]) > 8 or str(place[1]) > 'h':
            print(f"Invalid placement of {figure}")


isValidChessBoard(chess_board)