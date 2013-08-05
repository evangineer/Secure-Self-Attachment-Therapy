import os

# define the players
PARENT = 1
CHILD = 0

# create a standard matrix layout
def create_matrix_layout(t,u,v,w):
    return [[(t[0], t[1]), (u[0], u[1])], [(v[0], v[1]), (w[0], w[1])]]

# inverts logical bits (0 -> 1 and 1 -> 0)
def flip(x):
    return 1 - x

# checks to see if action defined by (p, c) is pareto optimal
def pareto_optimal(matrix, p, c):
    return  not better_strategy_for_both_exists(matrix, p, c, PARENT) and \
            not better_strategy_for_both_exists(matrix, p, c, CHILD)

# checks to see if action defined by (p, c) is a nash equilibrium
def nash_equilibrium(matrix, p, c):
    return  not alt_strategy_better_or_equal(matrix, p, c, PARENT) and \
            not alt_strategy_better_or_equal(matrix, p, c, CHILD)
            

# Given the opponent's strategy stays the same, is there a better strategy for 'player'?
def alt_strategy_better_or_equal(matrix, p, c, player):
    if player == PARENT:
        return matrix[p][c][player] <= matrix[flip(p)][c][player]
    if player == CHILD:
        return matrix[p][c][player] <= matrix[p][flip(c)][player]
    

# Does there exist a strategy that improves one gain without reducing the other's?
def better_strategy_for_both_exists(matrix, p, c, player):
    if player == PARENT:
        return matrix[p][c][PARENT] < matrix[flip(p)][c][PARENT]         and matrix[p][c][CHILD] <= matrix[flip(p)][c][CHILD] or \
               matrix[p][c][PARENT] < matrix[p][flip(c)][PARENT]         and matrix[p][c][CHILD] <= matrix[p][flip(c)][CHILD] or \
               matrix[p][c][PARENT] < matrix[flip(p)][flip(c)][PARENT] and matrix[p][c][CHILD] <= matrix[flip(p)][flip(c)][CHILD] 
    if player == CHILD:
        return matrix[p][c][CHILD] < matrix[flip(p)][c][CHILD]         and matrix[p][c][PARENT] <= matrix[flip(p)][c][PARENT] or \
               matrix[p][c][CHILD] < matrix[p][flip(c)][CHILD]         and matrix[p][c][PARENT] <= matrix[p][flip(c)][PARENT] or \
               matrix[p][c][CHILD] < matrix[flip(p)][flip(c)][CHILD] and matrix[p][c][PARENT] <= matrix[flip(p)][flip(c)][PARENT] 

