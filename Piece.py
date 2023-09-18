from BoardColor import *


class Piece:
    # definition of piece dimensions, moves, kings, colors
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False
        self.previousPosition = [0, 0]

    def move(self, row, column):
        self.previousPosition[self.row, self.column]
        self.row = row
        self.column = column

    def isKing(self):
        return self.king

    def makeKing(self):
        self.king = True

    def getCurrentPosition(self):
        return self.row, self.column

    def setCurrentPosition(self, row, column):
        self.row = row
        self.column = column

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __repr__(self) -> str:
        if self.color == AI_COLOR:
            return "AI"
        elif self.color == PLAYER_COLOR:
            return "PL"
