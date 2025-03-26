player, opponent = 'x', 'o'


def getReward(board):
    if board[0][0] != '_' and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == player:
            return 10
        else:
            return -10
    if board[1][0] != '_' and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == player:
            return 10
        else:
            return -10
    if board[2][0] != '_' and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == player:
            return 10
        else:
            return -10
    if board[0][0] != '_' and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == player:
            return 10
        else:
            return -10
    if board[0][1] != '_' and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] == player:
            return 10
        else:
            return -10
    if board[0][2] != '_' and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] == player:
            return 10
        else:
            return -10
    if board[0][0] != '_' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        else:
            return -10
    if board[0][2] != '_' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        else:
            return -10
    return 0


def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def minimax(board, depth, isMax):
    score = getReward(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if not isMovesLeft(board):
        return 0

    if isMovesLeft(board):
        if isMax:
            best = -float('inf')

            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = player
                        best = max(best, minimax(board, depth + 1, not isMax))
                        board[i][j] = "_"

            return best

        else:
            best = float('inf')

            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = opponent
                        best = min(best, minimax(board, depth + 1, not isMax))
                        board[i][j] = "_"

            return best


def findBestMove(board):
    best = -float('inf')
    bestMove = (-1,-1)
    result = []

    if getReward(board) == 10 or getReward(board) == -10:
        return bestMove

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player

                moveVal = minimax(board, 0, False)

                board[i][j] = '_'

                if moveVal > best:
                    bestMove = (i,j)
                    best = moveVal

    print("Best move:", bestMove)
    return bestMove

board = [
    ['x', 'x', 'o'],
    ['o', 'o', 'x'],
    ['_', '_', '_']
]

bestMove = findBestMove(board)

print("The Best Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])
