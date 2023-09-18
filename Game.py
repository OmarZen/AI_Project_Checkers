from time import sleep
from BoardColor import *
from tkinter import font
from Board import Board
import tkinter as tk


class Game:
    # tk frame  #tk button     #tk string  #tk string -> AI depth
    def __init__(self, Frame, TurnIndicator, Algorithm, Difficulty):
        self.button = None
        self.previousPlayerKingPiecesCounter = 0
        self.previousAIKingPiecesCounter = 0
        self.Turn = False
        self.run = True
        self.Frame2 = Frame
        self.Algorithm = Algorithm
        self.Difficulty = Difficulty
        self.Board = Board()
        self.previousBoard = None
        self.TurnIndicator = TurnIndicator
        self.ChangeTurnIndicator(AI_COLOR_STR)
        self.createBoard()
        self.movesCount = 0
        self.deathCount = 0
        self.previousAIPiecesCounter = 12
        self.previousPlayerPiecesCounter = 12
        self.WinnerIndicator = None

    def getPreviousBoard(self):  # Back Option
        if self.previousBoard and self.movesCount > 0 and self.WinnerIndicator != 1:
            self.movesCount -= 1
            self.Board = self.previousBoard
            self.previousBoard = None
            self.changeTurn()
            self.createBoard()

    def Play(self):  # GamePlay Setup
        if not self.run:
            return

        newBoard = self.Board.AI_MOVE(int(self.Difficulty.get()), self.Algorithm.get(), self.Turn)
        # sleep(0.75)
        if not newBoard or newBoard == self.Board:
            self.displayWinner(self.Board.getWinner())
            return

        # Assigns
        self.previousAIPiecesCounter = self.Board.AI_PIECES
        self.previousPlayerPiecesCounter = self.Board.PLAYER_PIECES
        self.previousAIKingPiecesCounter = self.Board.AI_King_Piece
        self.previousPlayerKingPiecesCounter = self.Board.Player_King_Piece

        self.previousBoard = self.Board
        self.Board = newBoard
        self.createBoard()
        self.changeTurn()
        self.movesCount += 1

        if self.movesCount >= 70:
            if (self.previousAIPiecesCounter == self.Board.AI_PIECES and
                    self.previousPlayerPiecesCounter == self.Board.PLAYER_PIECES and
                    self.previousAIKingPiecesCounter == self.Board.AI_King_Piece and
                    self.previousPlayerKingPiecesCounter == self.Board.Player_King_Piece):
                self.deathCount += 1
            else:
                self.deathCount = 0
        else:
            self.deathCount = 0

        if self.deathCount >= 20:
            self.displayWinner(self.Board.getWinner())

    def ResetButton(self):
        # calls the resetBoard() from the constructor
        self.__init__(self.Frame2, self.TurnIndicator, self.Algorithm, self.Difficulty)
        print("Reset")

    def ResetFrame(self):
        for item in self.Frame2.winfo_children():
            item.destroy()

    def createBoard(self):
        self.ResetFrame()
        counter = 0
        for i, row in enumerate(self.Board.getBoard()):
            for j, piece in enumerate(row):
                if counter % 2:
                    square = self.Square(BLOCK2_COLOR, i, j)
                else:
                    square = self.Square(BLOCK1_COLOR, i, j)

                if piece != 0 and piece.getColor() != VALID_COLOR:
                    self.Piece(square, piece)
                elif piece != 0 and piece.getColor() == VALID_COLOR:
                    self.Piece(square, piece)

                counter += 1
            counter += 1

    # Own config
    def Square(self, Color, Row, Column):
        # Game Window Frame
        square = tk.Frame(self.Frame2, background=Color, width=50, height=50)
        square.rowconfigure(0, weight=1)
        square.columnconfigure(0, weight=1)
        square.grid_propagate(False)
        square.grid(row=Row, column=Column)

        return square

    # Own config
    def Piece(self, Parent, piece):
        self.button = tk.Label(Parent, background=piece.getColor(), border=0)

        if piece.isKing():
            f = font.Font(family='Helvetica', size=14, weight='bold')
            self.button.config(text="♔", font=f, fg="gold")
        self.button.grid(sticky="NWSE", padx=10, pady=10)

    def changeTurn(self):
        self.Turn = not self.Turn
        if self.Turn:
            self.ChangeTurnIndicator(AI_COLOR_STR)
        else:  # Player turn
            self.ChangeTurnIndicator(PLAYER_COLOR_STR)

    # Own Config
    def ChangeTurnIndicator(self, Color):
        WinnerColor = self.Board.WinnerSide()  # returns winner color
        if WinnerColor is not None:
            self.displayWinner(WinnerColor)
            return

        self.TurnIndicator.config(background="#361500", text="Next Turn", foreground="White")
        self.TurnIndicator.update()

    # Own Config
    def displayWinner(self, winnerColor):
        self.run = False
        thisFont = font.Font(family='Helvetica', size=8, weight='bold')
        self.TurnIndicator.config(text=winnerColor + " WINS", font=thisFont, foreground="white", background=winnerColor)
        self.TurnIndicator.update()
        self.WinnerIndicator = 1
