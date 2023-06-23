"""
Tic Tac Toe Player
"""
import math
import copy

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
    count = 0
    #percorre a matriz (board) e verifica, se o numero for de count for impar vai ser vez do O (pq comeca sempre com X)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                count+=1
    if count%2 == 0:
        return X
    else:
        return O

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
        raise Exception("invalid.",action) 
    newboard = copy.deepcopy(board)
    newboard[action[0]][action[1]] = player(board)
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0 :
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
         
         return None
    
    #alterar x para o para ele ficar terrivel

    elif player(board) == X:
        return maxValue(board)[1] # max value 1 = X vence
    else:
        return minValue(board)[1] # min value -1 = O vence

    
def maxValue(board):

    v = float('-inf')
    # set() de opcoes em que o jogo acaba?
    optimal = None
    #se o jogo acabou retorna quem ganhou
    if terminal(board):
        return utility(board), None
     
    for action in actions(board):
        
        newv = minValue(result(board,action))[0]
        if newv > v:
            v = newv
            optimal = action
            if newv == 1:
                break
            

    return v, optimal
        
     
def minValue(board):

    v = float('inf')
     # set() de opcoes em que o jogo acaba?
    optimal = None
     #se o jogo acabou retorna quem ganhou
    if terminal(board):
         return utility(board), None
     
    for action in actions(board):
        
        newv = maxValue(result(board,action))[0]
        
        if newv < v:
            v = newv
            optimal = action
            if newv == -1:
                break
            
        
    return v,optimal



