# This script contains the game theory table and functions to run the iterated game

# The game theory matrix:
#
#                        Parent
#                   Attend    Ignore
#                |   4,4   |   2,3   |         |   t  |   u  |
#         Go     |_________|_________|         |______|______|
# Child          |         |         |         |      |      |
#       Don't Go |   3,1   |   3,2   |         |   v  |   w  |
#
#

import renpy.store as store
import renpy.exports as renpy
import game_logic_function

class GameLogic(store.object):

    # initialize all the member variables
    def __init__(self):
        self.t_default = [4.0,2.0]
        self.u_default = [2.0,3.0]
        self.v_default = [3.0,1.0]
        self.w_default = [3.0,4.0]
        
        self.t = [4.0,2.0]
        self.u = [2.0,3.0]
        self.v = [3.0,1.0]
        self.w = [3.0,4.0]

        # value to re-enforce adults attending
        self.r = 1.02
        # value to re-enforce inner child going
        self.s = 1.05

        self.round = 0
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
        
    def attend_go(self):
        self.t_count += 1
        self.round += 1
        
    def attend_dontgo(self):
        self.v_count += 1
        self.round += 1
        
    def ignore_go(self):
        self.u_count += 1
        self.round += 1
        
    def ignore_dontgo(self):
        self.w_count += 1
        self.round += 1

    def change_r(self,new_r):
        self.r = new_r
        
    def change_s(self,new_s):
        self.s = new_s
    
    # resets the matrix and the action counts    
    def reset(self):
        self.t = self.t_default
        self.u = self.u_default
        self.v = self.v_default
        self.w = self.w_default
        
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
    
    # checks if the action chosen is pareta optimal and a nash equilibrium    
    def check_win(self, attend, go):
        self.update_matrix()
        return game_logic_function.pareto_optimal(self.create_matrix(), not attend, not go) and game_logic_function.nash_equilibrium(self.create_matrix(), not attend , not go)

    # updates the matrix to the most recent values    
    def update_matrix(self):
        self.t[1] = self.t_default[1] * self.r ** self.t_count
        self.t[0] = self.t_default[0] * self.s ** self.t_count
        self.v[1] = self.v_default[1] * self.r ** self.v_count
        self.u[0] = self.u_default[0] * self.s ** self.u_count
    
    # setup matrix layout to be compatible with the functions in "game_logic_function"    
    def create_matrix(self):
        return game_logic_function.create_matrix_layout(self.t, self.u, self.v, self.w)

        

