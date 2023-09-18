from Piece import Piece
from Minimax import *
from AlphaBeta import *

ROWS = COLUMNS = 8


class Board:
    def __init__(self):
        self.AI_PIECES = 12
        self.PLAYER_PIECES = 12
        self.AI_King_Piece = 0
        self.Player_King_Piece = 0
        self.resetBoard()
        self.alpha = float('-inf')
        self.beta = float('inf')

    def resetBoard(self):
        self.Board = []
        counter = 0
        for row in range(ROWS):
            self.Board.append([])
            for column in range(COLUMNS):
                if counter % 2:
                    if row < 3:
                        self.Board[row].append(Piece(row, column, PLAYER_COLOR_STR))
                    elif row > 4:
                        self.Board[row].append(Piece(row, column, AI_COLOR_STR))
                    else:
                        self.Board[row].append(0)
                else:
                    self.Board[row].append(0)
                counter += 1
            counter += 1
        return self

    def getBoard(self):
        return self.Board

    def getAllPieces(self, color):
        allPieces = []
        for row in self.Board:
            for piece in row:
                if piece != 0 and piece.getColor() == color:
                    allPieces.append(piece)
        return allPieces

    # values changed
    def evaluateScore(self):
        Score = 0
        if self.WinnerSide() == AI_COLOR_STR:
            Score += 1000
        elif self.WinnerSide() == PLAYER_COLOR_STR:
            Score -= 1000
        Score += self.AI_PIECES - self.PLAYER_PIECES
        Score += self.AI_King_Piece * 0.5 - self.Player_King_Piece * 0.5
        return Score

    def getValidMoves(self, piece):
        moves = {}  # array of moves
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row
        try:
            if piece.getColor() == AI_COLOR_STR or piece.isKing():
                moves.update(self.traverseLeft(row - 1, max(row - 3, -1), -1, piece.color, left))
                moves.update(self.traverseRight(row - 1, max(row - 3, -1), -1, piece.color, right))
            if piece.getColor() == PLAYER_COLOR_STR or piece.isKing():
                moves.update(self.traverseLeft(row + 1, max(row + 3, 8), 1, piece.color, left))
                moves.update(self.traverseRight(row + 1, max(row + 3, 8), 1, piece.color, right))
        except:
            print("Left:", left)
            print("Right:", right)
        return moves

    def traverseLeft(self, Start, Stop, Step, Color, Left, SkippedPieces=None):
        if SkippedPieces is None:
            SkippedPieces = []

        moves = {}
        Last = []
        for i in range(Start, Stop, Step):
            if Left < 0:
                break

            Current = self.Board[i][Left]
            if Current == 0:
                if SkippedPieces and not Last:
                    break
                elif SkippedPieces:
                    moves[(i, Left)] = Last + SkippedPieces
                else:
                    moves[(i, Left)] = Last

                if Last:
                    if Step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, 8)
                    moves.update(self.traverseLeft(i + Step, row, Step, Color, Left - 1, SkippedPieces=Last))
                    moves.update(self.traverseRight(i + Step, row, Step, Color, Left + 1, SkippedPieces=Last))
                break
            elif Current.getColor() == Color:
                break
            else:
                Last = [Current]

            Left -= 1

        return moves

    def traverseRight(self, Start, Stop, Step, Color, Right, SkippedPieces=None):
        if SkippedPieces is None:
            SkippedPieces = []

        moves = {}
        Last = []
        for i in range(Start, Stop, Step):
            if Right >= COLUMNS:
                break

            Current = self.Board[i][Right]
            if Current == 0:
                if SkippedPieces and not Last:
                    break
                elif SkippedPieces:
                    moves[(i, Right)] = Last + SkippedPieces
                else:
                    moves[(i, Right)] = Last

                if Last:
                    if Step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, 8)
                    moves.update(self.traverseLeft(i + Step, row, Step, Color, Right - 1, SkippedPieces=Last))
                    moves.update(self.traverseRight(i + Step, row, Step, Color, Right + 1, SkippedPieces=Last))
                break
            elif Current.getColor() == Color:
                break
            else:
                Last = [Current]

            Right += 1

        return moves

    def removeSkippedPieces(self, SkippedPieces):
        try:
            for piece in SkippedPieces:
                pieceRow, pieceColumn = piece.getCurrentPosition()
                if piece.getColor() == PLAYER_COLOR_STR:
                    self.PLAYER_PIECES -= 1

                    if self.Board[pieceRow][pieceColumn]:
                        if piece.isKing():
                            self.Player_King_Piece -= 1

                else:  # if Color is -> AI_COLOR
                    self.AI_PIECES -= 1

                    if self.Board[pieceRow][pieceColumn]:
                        if piece.isKing():
                            self.AI_King_Piece -= 1

                self.Board[pieceRow][pieceColumn] = 0
        except:  # finally
            print("Error Occurred the piece can't be removed")

    def move(self, piece, newPosition, SkippedPieces):  # Computer/Player Move
        mainRow, mainColumn = piece.getCurrentPosition()
        piece.previousPosition = [mainRow, mainColumn]
        row = newPosition[0]
        column = newPosition[1]
        self.Board[mainRow][mainColumn] = 0
        self.removeSkippedPieces(SkippedPieces)

        if piece.getColor() == PLAYER_COLOR_STR:
            if row == ROWS - 1 and not piece.isKing():
                piece.makeKing()
                self.AI_King_Piece += 1
            piece.setCurrentPosition(row, column)
            self.Board[row][column] = piece

        else:
            if row == 0 and not piece.isKing():
                piece.makeKing()
                self.Player_King_Piece += 1
            piece.setCurrentPosition(row, column)
            self.Board[row][column] = piece

    def AI_MOVE(self, Difficulty, Algorithm, Player):  # Difficulty -> Search Depth , Player -> turn based on color
        if Algorithm == "Minimax":
            temp = minimax(self, Difficulty, Player)
            return temp[1]
        else:  # Algorithm is Alpha-Beta (Minimax refinement)
            temp = alphabeta(self, Difficulty, not Player)
            return temp[1]

    def WinnerSide(self):  # check who wins the game, if all the pieces were eaten
        if self.AI_PIECES <= 0:
            return PLAYER_COLOR_STR  # PLAYER_COLOR
        elif self.PLAYER_PIECES <= 0:
            return AI_COLOR_STR  # AI_COLOR
        return None

    def getWinner(self):
        # get the winner when there are no eligible moves left (winner who has the most pieces on the board)
        if self.PLAYER_PIECES < self.AI_PIECES:
            return AI_COLOR_STR  # AI_COLOR
        return PLAYER_COLOR_STR  # PLAYER_COLOR
