import copy

X = "X"
O = "O"
EMPTY = None


board = [[O, O, X],
        [O, X, EMPTY],
    [EMPTY, O, EMPTY]]




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("invalid.") 
    newboard = copy.deepcopy(board)
    newboard[action[0]][action[1]] = X
    return newboard


print(result(board,(1,2)))