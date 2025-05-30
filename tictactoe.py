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

    possible_actions = list()

    for l in range(len(board)):
        for c in range(len(board[l])):
            if board[l][c] == EMPTY:
                possible_actions.append(l, c)

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

    winner_set = set()

    for l in range (3):
        if (board[l][0] == board[l][1] == board[l][2]) and (board[l][0] != EMPTY):
            # return X if board[l][0] == "X" else O
            winner_set.add(board[l][0])
    
    for c in range (3):
        if (board[0][c] == board[1][c] == board [2][c]) and (board[0][c] != EMPTY):
            # return X if board[0][c] == "X" else O
            winner_set.add(board[0][c])
        
    if (board[0][0] == board[1][1] == board [2][2]) and (board[0][0] != EMPTY):
            # return X if board[0][0] == "X" else O
            winner_set.add(board[0][0])
    
    if (board[2][0] == board[1][1] == board [0][2]) and (board[2][0] != EMPTY):
            # return X if board[2][0] == "X" else O
            winner_set.add(board[2][0])


    if len(winner_set) > 1:
        raise ValueError("Tabuleiro inválido: Dois vencedores ")
    
    if "X" in winner_set:
        return X
    
    elif "O" in winner_set:
        return O
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    
    for l in range(len(board)):
        for c in range(len(board[l])):
            if board[l][c] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1
    
    else:
        return 0
    

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    '''
        buscar as minhas ações

        Para cada ação, buscar as ações adversárias

            para cada ação adversária, 
                ver o resultado.
                salvar a utilidade em um conjunto
        
        descobrir as ações válidas através do máximo valor mínimo
        
        
    '''

    if terminal(board):
        return None

'''
    if player(board) == X:

        my_possible_actions = actions(board)

        my_utility_list = list()
        

        for my_action in my_possible_actions:

            # l, c = my_action

            board_1 = result(board, my_action)

            adv_possible_actions = actions(board_1)

            adv_action_utility = list()

            for adv_action in adv_possible_actions:
            
                # i, j = adv_action

                board_2 = result(board_1, adv_action)

                adv_action_utility.append(utility(board_2))

            my_utility_list.append(min(adv_action_utility))

        max_util = my_utility_list.index(max(my_utility_list))

        return my_possible_actions[max_util]
        
'''

            





            



    raise NotImplementedError





# inicio = initial_state()
# print(player(inicio))
# print(actions(inicio))
# print(result(inicio,(0,2)))
# print(f'{inicio}')