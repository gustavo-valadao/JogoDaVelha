"""
Tic Tac Toe Player
"""

import math
import copy

# Possíveis movimentos:
X = "X"
O = "O"
EMPTY = None


possible_moves = [0, 1, 2, 4, 5, 6, 7, 8]



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

    return X if len(possible_moves)%2 == 0 else O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = []

    for move in possible_moves:
        i = move//3
        j = move % 3
        possible_actions.append((i, j))

    return possible_actions
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    l, c = action

    if board[l][c] is not EMPTY:
        raise ValueError("Movimento inválido: A casa está ocupada")
    
    if l >= len(board) or l <= 0 or c >= len(board[l]) or c < 0:
        raise ValueError("Movimento inválido: fora dos limites do tabuleiro")
    
    board_result = copy.deepcopy(board)
    board_result[l][c] = player(board)

    return board_result


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError





# inicio = initial_state()
# print(player(inicio))
# print(actions(inicio))
# print(result(inicio,(0,2)))
# print(f'{inicio}')