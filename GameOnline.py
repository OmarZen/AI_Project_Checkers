from BoardOnline import BoardOnline
import time
import random
from Minimax import *
from AlphaBeta import *
from Board import Board
from Piece import Piece
from Game import Game


# GAME LINK
# https://cardgames.io/checkers/


def main():
    board = BoardOnline()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        # for piece in allPieces:
        #     pieceRow, pieceColumn = piece.getCurrentPosition()
        #     board.select_dimension(pieceRow, pieceColumn)
        allPieces = Board.getAllPieces(AI_COLOR_STR)
        for piece in allPieces:
            newBoard = Board.AI_MOVE(3, "AlphaBeta", False)
            tempBoard = newBoard[piece.row][piece.column]
            board.select_dimension(piece.row, piece.column)

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)

        time.sleep(2)


if __name__ == "__main__":
    main()
