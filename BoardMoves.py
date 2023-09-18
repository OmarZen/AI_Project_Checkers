from copy import deepcopy


def simulate_move(piece, move, board, skippedPieces):
    board.move(piece, move, skippedPieces)
    return board


def getAllBoards(board, color):
    boards = []

    for piece in board.getAllPieces(color):
        validMoves = board.getValidMoves(piece)
        for move, skippedPieces in validMoves.items():
            tempBoard = deepcopy(board)
            tempPiece = tempBoard.getBoard()[piece.row][piece.column]
            newBoard = simulate_move(tempPiece, move, tempBoard, skippedPieces)
            boards.append(newBoard)
    return boards
