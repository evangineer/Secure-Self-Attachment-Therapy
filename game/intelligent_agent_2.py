# This script contains the Intelligent Agent used in the game to guide the user. 
# It is based on Cai Zhou's intelligent agent. It uses the GameLogic class and uses
# MDP, Q-learning algoritm and Ordinal Matrices to imitate the players, both adult and child.

# Q-learning equation: Q(s,a)' <- Q(s,a) + l*[R(s,s') + d*max[Q(s',a')] - Q(s,a)] 
#       where l: learning rate
#             d: discount factor

# Ordinal Matrix of parent:  from avoidant:  2 | 3    to secure:  4 | 3
#                                            -----                -----
#                                            1 | 4                1 | 2
#
# Ordinal Matrix of child: from avoidant:    4 | 2    to secure:  2 | 3
#                                            -----                -----
#                                            3 | 3                1 | 4

# Parent's MDP:   t | u   where t: attend & go
#                 -----         u: ignore & go
#                 v | w         v: attend & dont'go
#                               w: ignore & don't go
#
# Child's MDP:    o | p   where o: attend & go
#                 -----         p: ignore & go
#                 q | y         q: attend & don't go
#                               y: ignore & don't go

# AI Flow Chart:
#                                                               
#     -------> Action ----------- Ordinal matrix -------------\
#                 |                                       No   | State Change?
#                  \--------------- Probability --------------/|
#                               |                              | Yes
#                                \--------- Q-Values ---------/
#

import renpy.store as store
import renpy.exports as renpy
from game_logic import GameLogic
import random

class IntelligentAgent2(store.object):
    
    # initialize all the member variables
    def __init__(self):
        # AI contains the Game Logic
        self.ai_logic = GameLogic()
        # discount factor in the Q-learning algorithm
        self.discount = 0.4
        # k value for exploration
        self.k = 2
        
        # Set up for Parent
        self.p_change = 0
        
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
        
        # setup and initialize ordinal matrix
        self.p_ord_matrix = []
        self.ord_t = 0
        self.ord_u = 0
        self.ord_v = 0
        self.ord_w = 0
        self.update_p_ord_matrix()
        self.save_p_ord_matrix()
        
        # setup and initialize Q-value matrix
        self.q_t = self.ai_logic.t[1]
        self.q_u = self.ai_logic.u[1]
        self.q_v = self.ai_logic.v[1]
        self.q_w = self.ai_logic.w[1]
        self.p_q_matrix = []
        self.update_p_q_matrix()
        
        # setup and initialize probability matrix
        self.p_probability_matrix = []
        self.update_p_probability_matrix()
        
        # Set up for Child
        self.c_change = 0
        
        self.o_count = 0
        self.p_count = 0
        self.q_count = 0
        self.y_count = 0
        
        # setup and initialize ordinal matrix
        self.c_ord_matrix = []
        self.ord_o = 0
        self.ord_p = 0
        self.ord_q = 0
        self.ord_y = 0
        self.update_c_ord_matrix()
        self.save_c_ord_matrix()
        
        # setup and initialize Q-value matrix
        self.q_o = self.ai_logic.t[0]
        self.q_p = self.ai_logic.u[0]
        self.q_q = self.ai_logic.v[0]
        self.q_y = self.ai_logic.w[0]
        self.c_q_matrix = []
        self.update_c_q_matrix()
        
        # setup and initialize probability matrix
        self.c_probability_matrix = []
        self.update_c_probability_matrix()
        
    def reset_p_learning_rate(self):
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
        
    def reset_c_learning_rate(self):
        self.o_count = 0
        self.p_count = 0
        self.q_count = 0
        self.y_count = 0
        
    # function to calculate new ordinal matrix with new state and store the ordinal matrix    
    def update_ord_matrix(self):
        self.update_p_ord_matrix()
        self.update_c_ord_matrix()
    
    def update_p_ord_matrix(self):
        self.ai_logic.update_matrix()
        self.p_ord_matrix = []
        temp_matrix = [self.ai_logic.t[1], self.ai_logic.u[1], self.ai_logic.v[1], self.ai_logic.w[1]]
        
        # for each action, rank the reward in terms of value. Giving a matrix representing 41 states
        for i in range(4):
            count = 1
            for j in range(4):
                if i == j:
                    continue
                if temp_matrix[i] > temp_matrix[j]:
                    count += 1
            self.p_ord_matrix.append(count)

    def update_c_ord_matrix(self):
        self.ai_logic.update_matrix()
        self.c_ord_matrix = []
        temp_matrix = [self.ai_logic.t[0], self.ai_logic.u[0], self.ai_logic.v[0], self.ai_logic.w[0]]
        
        for i in range(4):
            count = 1
            for j in range(4):
                if i == j:
                    continue
                if temp_matrix[i] > temp_matrix[j]:
                    count += 1
            self.c_ord_matrix.append(count)
            
    # store ordinal values in the class to remember    
    def save_p_ord_matrix(self):
        self.ord_t = self.p_ord_matrix[0]
        self.ord_u = self.p_ord_matrix[1]
        self.ord_v = self.p_ord_matrix[2]
        self.ord_w = self.p_ord_matrix[3]
          
    def save_c_ord_matrix(self):
        self.ord_o = self.c_ord_matrix[0]
        self.ord_p = self.c_ord_matrix[1]
        self.ord_q = self.c_ord_matrix[2]
        self.ord_y = self.c_ord_matrix[3]
        
    # checks if the new calculated ordinal matrix is different to the old one, representing a change in state    
    def ord_matrix_change(self):
        parent = self.p_ord_matrix_change()
        child = self.c_ord_matrix_change()
        if child == True or parent == True:
            return True
        else:
            return False
    
    def p_ord_matrix_change(self):
        if (self.ord_t != self.p_ord_matrix[0] or self.ord_u != self.p_ord_matrix[1] or self.ord_v != self.p_ord_matrix[2] or self.ord_w != self.p_ord_matrix[3]):
            self.save_p_ord_matrix()
            self.p_change += 1
            self.reset_p_learning_rate()
            return True
        return False
        
    def c_ord_matrix_change(self):
        if (self.ord_o != self.c_ord_matrix[0] or self.ord_p != self.c_ord_matrix[1] or self.ord_q != self.c_ord_matrix[2] or self.ord_y != self.c_ord_matrix[3]):
            self.save_c_ord_matrix()
            self.c_change += 1
            self.reset_c_learning_rate()
            return True
        return False
    
    # updates the q matrix with new values of Q for each state change 
    def update_q_matrix(self):
        self.update_p_q_matrix()
        self.update_c_q_matrix()
    
    def update_p_q_matrix(self):
        self.p_q_matrix = []
        self.p_q_matrix.append(self.q_t)
        self.p_q_matrix.append(self.q_u)
        self.p_q_matrix.append(self.q_v)
        self.p_q_matrix.append(self.q_w)
        
    def update_c_q_matrix(self):
        self.c_q_matrix = []
        self.c_q_matrix.append(self.q_o)
        self.c_q_matrix.append(self.q_p)
        self.c_q_matrix.append(self.q_q)
        self.c_q_matrix.append(self.q_y)
        
    # updates the Q value for action t    
    def update_q_t(self):
        if self.t_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.t_count
        self.q_t = self.q_t + learning_rate*(self.ai_logic.t[1] + (self.discount * max(self.p_q_matrix)) - self.q_t)
    
    # updates the Q value for action u    
    def update_q_u(self):
        if self.u_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.u_count
        self.q_u = self.q_u + learning_rate*(self.ai_logic.u[1] + (self.discount * max(self.p_q_matrix)) - self.q_u)
    
    # updates the Q value for action v    
    def update_q_v(self):
        if self.v_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.v_count
        self.q_v = self.q_v + learning_rate*(self.ai_logic.v[1] + (self.discount * max(self.p_q_matrix)) - self.q_v)
    
    # updates the Q value for action w    
    def update_q_w(self):
        if self.w_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.w_count
        self.q_w = self.q_w + learning_rate*(self.ai_logic.w[1] + (self.discount * max(self.p_q_matrix)) - self.q_w)
        
    # updates the Q value for action o   
    def update_q_o(self):
        if self.o_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.o_count
        self.q_o = self.q_o + learning_rate*(self.ai_logic.t[0] + (self.discount * max(self.c_q_matrix)) - self.q_o)
    
    # updates the Q value for action p    
    def update_q_p(self):
        if self.p_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.p_count
        self.q_p = self.q_p + learning_rate*(self.ai_logic.u[0] + (self.discount * max(self.c_q_matrix)) - self.q_p)
    
    # updates the Q value for action q    
    def update_q_q(self):
        if self.q_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.q_count
        self.q_q = self.q_q + learning_rate*(self.ai_logic.v[0] + (self.discount * max(self.c_q_matrix)) - self.q_q)
    
    # updates the Q value for action y    
    def update_q_y(self):
        if self.y_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.y_count
        self.q_y = self.q_y + learning_rate*(self.ai_logic.w[0] + (self.discount * max(self.c_q_matrix)) - self.q_y)
        
    # updates the probability matrix after a change in Q values    
    def update_probability_matrix(self):
        self.update_p_probability_matrix()
        self.update_c_probability_matrix()
    
    def update_p_probability_matrix(self):
        self.p_probability_matrix = []
        self.update_p_q_matrix()
        total = 0
        for i in range(4):
            total += self.k ** self.p_q_matrix[i]
        self.p_probability_matrix.append((self.k**self.q_t)/total)
        self.p_probability_matrix.append((self.k**self.q_u)/total)
        self.p_probability_matrix.append((self.k**self.q_v)/total)
        self.p_probability_matrix.append((self.k**self.q_w)/total)
        
    def update_c_probability_matrix(self):
        self.c_probability_matrix = []
        self.update_c_q_matrix()
        total = 0
        for i in range(4):
            total += self.k ** self.c_q_matrix[i]
        self.c_probability_matrix.append((self.k**self.q_o)/total)
        self.c_probability_matrix.append((self.k**self.q_p)/total)
        self.c_probability_matrix.append((self.k**self.q_q)/total)
        self.c_probability_matrix.append((self.k**self.q_y)/total)
        
    # checks if the AI won the game given an action pair    
    def check_win(self, adult, child):
        return self.ai_logic.check_win(adult, child)
    
    # returns the number of rounds the AI has played    
    def get_round(self):
        return self.ai_logic.round
    
    def parent_move(self):
        # random number from 0 to 1
        choice = random.random()
        # determine the probablistic range of each action
        prob_t = self.p_probability_matrix[0]
        prob_u = self.p_probability_matrix[0]+self.p_probability_matrix[1]
        prob_v = self.p_probability_matrix[0]+self.p_probability_matrix[1]+self.p_probability_matrix[2]
        prob_w = 1
        
        # if t is chosen, adult attends
        if choice < prob_t:
            adult = "attend"
            
        # if u is chosen, adult ignores
        if prob_t <= choice and choice < prob_u:
            adult = "ignore"
            
        # if v is chosen, adult attends
        if prob_u <= choice and choice < prob_v:
            adult = "attend"
            
        # if w is chosen, adult ignores
        if prob_v <= choice and choice < prob_w:
            adult = "ignore"
            
        return adult
    
    def child_move(self):
        # random number from 0 to 1
        choice = random.random()
        # determine the probablistic range of each action
        prob_o = self.c_probability_matrix[0]
        prob_p = self.c_probability_matrix[0]+self.c_probability_matrix[1]
        prob_q = self.c_probability_matrix[0]+self.c_probability_matrix[1]+self.c_probability_matrix[2]
        prob_y = 1
        
        # if t is chosen, adult attends
        if choice < prob_o:
            child = "go"
            
        # if u is chosen, adult ignores
        if prob_o <= choice and choice < prob_p:
            child = "go"
            
        # if v is chosen, adult attends
        if prob_p <= choice and choice < prob_q:
            child = "dontgo"
            
        # if w is chosen, adult ignores
        if prob_q <= choice and choice < prob_y:
            child = "dontgo"
            
        return child
    
    def move(self):
        adult = self.parent_move()
        child = self.child_move()
        
        # find which action was chosen and update the specific Q value and probability matrix
        if adult == "attend" and child == "go":
            self.ai_logic.attend_go()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            # checks if the action caused a change in the ordinal matrix
            self.ord_matrix_change()
            if not self.check_final_action("adult"):
                self.t_count += 1
                self.update_q_t()
            if not self.check_final_action("child"):
                self.o_count += 1
                self.update_q_o()
            self.update_q_matrix()
            self.update_probability_matrix()
            
        if adult == "attend" and child == "dontgo":
            self.ai_logic.attend_dontgo()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            self.ord_matrix_change()
            if not self.check_final_action("adult"):
                self.v_count += 1
                self.update_q_v()
            if not self.check_final_action("child"):
                self.q_count += 1
                self.update_q_q()
            self.update_q_matrix()
            self.update_probability_matrix()
            
        if adult == "ignore" and child == "go":
            self.ai_logic.ignore_go()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            self.ord_matrix_change()
            if not self.check_final_action("adult"):
                self.u_count += 1
                self.update_q_u()
            if not self.check_final_action("child"):
                self.update_q_p()
                self.p_count += 1
            self.update_q_matrix()
            self.update_probability_matrix()
                   
        if adult == "ignore" and child == "dontgo":
            self.ai_logic.ignore_dontgo()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            self.ord_matrix_change()
            if not self.check_final_action("adult"):
                self.w_count += 1
                self.update_q_w()
            if not self.check_final_action("child"):
                self.y_count += 1
                self.update_q_y()
            self.update_q_matrix()
            self.update_probability_matrix()
                
        return [adult, child]
        
    def check_final_action(self, player):
        if player == "adult":
            for i in range(4):
                if round(self.p_probability_matrix[i], 2) == 1.00:
                    return True
            return False
        elif player == "child":
            for i in range(4):
                if round(self.c_probability_matrix[i], 2) == 1.00:
                    return True
            return False
        
        