from BoardColor import *
from BoardMoves import *
import random


def alphabeta(position, depth, maxPlayer):
    if depth == 0 or position.WinnerSide() is not None:
        return position.evaluateScore(), position

    if maxPlayer:
        maxVal = float('-inf')
        allBoards = getAllBoards(position, AI_COLOR_STR)

        if not allBoards:
            return float('-inf'), position
        index = random.randint(0, len(allBoards) - 1)
        bestMove = allBoards[index]

        for move in allBoards[1:]:
            value = alphabeta(position, depth - 1, False)[0]
            maxVal = max(value, maxVal)
            position.alpha = max(position.alpha, maxVal)
            if position.beta <= position.alpha:
                bestMove = move
                break
        return maxVal, bestMove
    else:  # minPlayer
        minVal = float('inf')
        allBoards = getAllBoards(position, PLAYER_COLOR_STR)

        if not allBoards:
            return float('inf'), position
        index = random.randint(0, len(allBoards) - 1)
        bestMove = allBoards[index]

        for move in allBoards[1:]:
            value = alphabeta(position, depth - 1, True)[0]
            minVal = min(value, minVal)
            position.beta = min(position.beta, minVal)
            if position.beta <= position.alpha:
                bestMove = move
                break
        return minVal, bestMove
