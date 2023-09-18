from BoardColor import *
from BoardMoves import *


def minimax(position, depth, maxPlayer):
    if depth == 0 or position.WinnerSide() is not None:
        return position.evaluateScore(), position

    if maxPlayer:
        maxEvaluate = float('-inf')
        bestBoard = None

        allBoards = getAllBoards(position, PLAYER_COLOR_STR)
        if not allBoards:
            return float('-inf'), position

        for board in allBoards:
            evaluation = minimax(board, depth - 1, False)[0]
            maxEvaluate = max(maxEvaluate, evaluation)
            if maxEvaluate == evaluation:
                bestBoard = board
        return maxEvaluate, bestBoard

    else:  # minPlayer
        minEvaluation = float('inf')
        bestBoard = None

        allBoards = getAllBoards(position, AI_COLOR_STR)

        if not allBoards:
            return float('inf'), position

        for board in allBoards:
            evaluation = minimax(board, depth - 1, True)[0]
            minEvaluation = min(minEvaluation, evaluation)
            if minEvaluation == evaluation:
                bestBoard = board
        return minEvaluation, bestBoard
