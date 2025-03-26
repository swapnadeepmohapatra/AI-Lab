player, opponent = 'x', 'o'

def getReward(board):
    # Check rows, columns, and diagonals in a loop
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            return 10 if board[i][0] == player else -10
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            return 10 if board[0][i] == player else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == player else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == player else -10

    return 0

def isMovesLeft(board):
    return any('_' in row for row in board)

def minimax(board, depth, isMax):
    score = getReward(board)

    if score in [10, -10]:  # If game is won, return score
        return score

    if not isMovesLeft(board):  # If no moves left, it's a draw
        return 0

    best = -float('inf') if isMax else float('inf')
    current_player = player if isMax else opponent

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = current_player
                best = max(best, minimax(board, depth + 1, not isMax)) if isMax else min(best, minimax(board, depth + 1, not isMax))
                board[i][j] = '_'

    return best

def findBestMove(board):
    best = -float('inf')
    bestMove = (-1, -1)

    if getReward(board) in [10, -10]:  # If game is already won, return no move
        return bestMove

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'

                if moveVal > best:
                    bestMove = (i, j)
                    best = moveVal

    return bestMove

# Example board
board = [
    ['x', 'x', 'o'],
    ['o', 'o', 'x'],
    ['_', '_', '_']
]

bestMove = findBestMove(board)
print("The Best Move is: ROW:", bestMove[0], " COL:", bestMove[1])
