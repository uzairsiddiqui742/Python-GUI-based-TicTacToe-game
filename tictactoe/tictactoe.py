"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return "X"
    if terminal(board):
        return "Game Over"
    else:
        countX = 0
        countO = 0
        for i in board:
            for j in i:
                if j == X:
                    countX += 1
                if j == O:
                    countO += 1

        if countX > countO:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    list2 = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                list2.add((row, col))
    return list2


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    tempBoard = copy.deepcopy(board)

    if tempBoard[action[0]][action[1]] is not None:
        raise Exception("Invalid Move")
    else:
        playerMove = player(tempBoard)
        tempBoard[action[0]][action[1]] = playerMove
        return tempBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Diagonal Check
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    # Horizontal and Vertical check
    for i in range(3):
        if (board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X") or (
                board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X"):
            return "X"
        if (board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O") or (
                board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O"):
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        print("max: ", aux)
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    print("Final max", v)
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        print("min:", aux)
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    print("Final min", v)
    return v, move
