"""
Tic Tac Toe Player
"""

import math
import copy
import random

# Possíveis movimentos:
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
    X_marks = 0
    O_marks = 0

    for l in range(len(board)):
        X_marks += board[l].count("X")
        O_marks += board[l].count("O")


    return X if X_marks==O_marks else O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = list()

    for l in range(len(board)):
        for c in range(len(board[l])):
            if board[l][c] == EMPTY:
                possible_actions.append((l, c))

    return possible_actions
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    l, c = action

    if l >= len(board) or l < 0 or c >= len(board[l]) or c < 0:
        raise ValueError("Movimento inválido: fora dos limites do tabuleiro")
    
    if board[l][c] is not EMPTY:
        raise ValueError("Movimento inválido: A casa está ocupada")
    
    current_player = player(board)

    board_result = copy.deepcopy(board)
    board_result[l][c] = current_player

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



    '''
    FUNÇÃO MINIMAX COM PODA ALFA BETA: 

        Ver se a posição é terminal. Se sim, retorna None

        Verificar o jogador:

            Se for X (busca maior valor):

                Inicializar:
                    VALOR_MÁXIMO como -infinito (qualquer ganho é lucro)

                Inicializar:
                    ALFA (-inf)  - melhor pontuação que X pode garantir até agora
                    BETA (+inf)  - melhor pontuação que Y pode garantir até agora


                define as jogadas possíveis. Para cada jogada:

                    Simula o tabuleiro

                    Roda a função que busca MÁXIMO_VALOR, passando (TABULEIRO,  ALFA e BETA), que retornará (Valor da utility e Melhor Jogada)

                        > Verifica se o tabuleiro é terminal, 
                            >> se sim retorna 
                                >> sua utility  (1, 0 , -1)
                                >> None para a jogada.
                            
                            >> não tendo sido retornado, continua...
                            
                            >> define o valor como - infinito
                            >> define a melhor jogada como None (ainda não descobrimos)

                                >> busca as ações adversárias, 
                                >> simula o tabuleiro 
                                >> roda a função que retorna MÍNIMO_VALOR , com os mesmos ALFA E BETA
                        
                    Analisar o retorno: 
                        > Se o valor do retorno for que o VALOR_MÁXIMO, atualiza o valor máximo
                        > Se o valor do retorno for maior ALFA, atualiza ALFA 
                        > Se o ALFA >= BETA, faz a poda interrompendo o loop (break)
                            Obs:  - o loop continuará até que todas as jogadas sejam avaliadas ou até que a poda ocorra. 
                                  - No final, teremos o melhor valor possível para X.
                    

            Se for O (busca o menor valor)

                (Idem, exceto que... )
                    * Inicializa como MÍNIMO_VALOR, que começará com +infinito (qualquer redução é lucro)
                    * Obs: ALFA E BETA são inicializados igualmente, pois são relativos aos jogadores (e não ao "jogador atual")

                    * Roda a função de MÍNIMO VALOR (idem à máximo valor, exceto que...)

                    * Ao comparar o resultado, busca o menor valor

                        ** Chama recursivamente a função do adversário (agora com MAX)
                        ** Se o valor retornado for menor que VALOR_MÍNIMO, atualiza
                        ** Se o valor retornado for menor que BETA, atualiza
                        ** Se ALFA >= BETA, faz a poda e encerra o loop

                    * OBS: A verificação de poda (ALFA >= BETA) é igual nas duas verificações!

                    
        OBSERVAÇÃO: MAIOR ALEATORIEDADE.
            > Optei por adicionar todas as best actions em uma lista, e retornar uma delas aleatoriamente.
            > Isso pq a lógica estava sempre começando na primeira casa [0][0], o que ficava chato.
            > Ele encontrava essa opção ao percorrer as actions, e nunca a atualizava, pois todas as demais eram iguais.
            > Assim, se existem mais de uma best_action, a lógica poderá jogar em resultados distintos.
            > Dito isso, a atualização "if action_utility > max_utility: best_action = [action]" é feita dessa maneira
              para resetar a lista de best actions anteriores, caso ele encontre um cenário com maior utilidade.
    '''


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None



    actual_player = player(board)

    if actual_player == X:

        best_action = []
        max_utility = -math.inf
        alfa = -math.inf
        beta = math.inf

        
        my_actions = actions(board)

        for action in my_actions:

            action_result = result(board, action)
            action_utility = min_function (action_result, alfa, beta)

            if action_utility > max_utility:
                max_utility = action_utility 
                best_action = [action]

            if action_utility == max_utility:
                best_action.append(action)


            if action_utility > alfa:
                alfa = action_utility 

            if alfa > beta:
                break
                
        return random.choice(best_action)
    


    elif actual_player == O:

        best_action= []
        min_utility = math.inf
        alfa = -math.inf
        beta = math.inf

        my_actions = actions(board)

        for action in my_actions:
            
            action_result = result(board, action)
            action_utility = max_function (action_result, alfa, beta)

            if action_utility < min_utility:
                min_utility = action_utility
                best_action = [action]
            
            if action_utility == min_utility:
                best_action.append(action)

            if action_utility < beta:
                beta = action_utility

            if alfa > beta:
                break
        
        return random.choice(best_action)

            
        
def max_function (board, alfa, beta):
    
    if terminal(board):
        return utility(board)
    
    node_utility = -math.inf
    node_alfa = alfa

    node_actions = actions(board)

    for action in node_actions:
        
        action_result = result(board, action)
        action_utility = min_function(action_result, node_alfa, beta)

        if action_utility > node_utility:
            node_utility = action_utility 

        if action_utility > node_alfa:
            node_alfa = action_utility

        if node_alfa > beta:
            break

    return node_utility



def min_function (board, alfa, beta):
    
    if terminal(board):
        return utility(board)
    
    node_utility = +math.inf
    node_beta = beta

    node_actions = actions(board)
    for action in node_actions:
        
        action_result = result(board, action)
        action_utility = max_function(action_result, alfa, node_beta)

        if action_utility < node_utility:
            node_utility = action_utility 

        if action_utility < node_beta:
            node_beta = action_utility

        if alfa > node_beta:
            break

    return node_utility




    '''
        buscar as minhas ações

        Para cada ação, buscar as ações adversárias

            para cada ação adversária, 
                ver o resultado.
                salvar a utilidade em um conjunto
        
        descobrir as ações válidas através do máximo valor mínimo
        
        
    '''
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