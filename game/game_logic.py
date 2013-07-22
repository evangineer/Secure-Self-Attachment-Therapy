# This script contains the game theory table and functions to run the iterated game

# The game theory matrix:
#
#                      Parent
#                 Attend    Ignore
#              |   4,4   |   2,3   |         |   t  |   u  |
#         Go   |_________|_________|         |______|______|
# Child        |         |         |         |      |      |
#       Ignore |   3,1   |   3,2   |         |   v  |   w  |
#
#

import renpy.store as store
import renpy.exports as renpy

class GameLogic(store.object):

    def __init__(self):
        self.t_default = [4,4]
        self.u_default = [2,3]
        self.v_default = [3,1]
        self.w_default = [3,2]
        
        self.t = [4,4]
        self.u = [2,3]
        self.v = [3,1]
        self.w = [3,2]

        self.r = 1.02
        self.s = 1.05

        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
        
    def attend_go(self):
        self.t_count += 1
        
    def attend_dontgo(self):
        self.v_count += 1
        
    def ignore_go(self):
        self.u_count += 1
        
    def ignore_dontgo(self):
        self.w_count += 1

    def change_r(self,new_r):
        self.r = new_r
        
    def change_s(self,new_s):
        self.s = new_s
        
    def update_matrix(self):
        self.t[0] = self.t_default[0] * self.r ** self.t_count
        self.t[1] = self.t_default[1] * self.s ** self.t_count
        self.v[0] = self.v_default[0] * self.r ** self.v_count
        self.u[1] = self.u_default[1] * self.s ** self.u_count
        

