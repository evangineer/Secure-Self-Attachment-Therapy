# This script contains the Intelligent Agent used in the game to guide the user. It uses the GameLogic class and uses
# MDP, Q-learning algoritm and Ordinal Matrices to imitate the player.

# Q-learning equation: Q(s,a)' <- Q(s,a) + l*[R(s,s') + d*max[Q(s',a')] - Q(s,a)] 
#       where l: learning rate
#             d: discount factor

# Ordinal Matrix:  from avoidant:  2 | 3    to secure:  4 | 3
#                                  -----                -----
#                                  1 | 4                1 | 2

# MDP:   t | u   where t: attend & go
#        -----         u: ignore & go
#        v | w         v: attend & dont'go
#                      w: ignore & don't go

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

class IntelligentAgent(store.object):
    
    # initialize all the member variables
    def __init__(self):
        # AI contains the Game Logic
        self.ai_logic = GameLogic()
        # discount factor in the Q-learning algorithm
        self.discount = 0.4
        # k value for exploration
        self.k = 2
        self.adult_last_move = "first"
        self.change = 0
        
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
        
        # setup and initialize ordinal matrix
        self.ord_matrix = []
        self.ord_t = 0
        self.ord_u = 0
        self.ord_v = 0
        self.ord_w = 0
        self.update_ord_matrix()
        self.save_ord_matrix()
        
        # setup and initialize Q-value matrix
        self.q_t = self.ai_logic.t[1]
        self.q_u = self.ai_logic.u[1]
        self.q_v = self.ai_logic.v[1]
        self.q_w = self.ai_logic.w[1]
        self.q_matrix = []
        self.update_q_matrix()
        
        # setup and initialize probability matrix
        self.probability_matrix = []
        self.update_probability_matrix()
        
    def reset_learning_rate(self):
        self.t_count = 0
        self.u_count = 0
        self.v_count = 0
        self.w_count = 0
    
    # function to calculate new ordinal matrix with new state and store the ordinal matrix    
    def update_ord_matrix(self):
        self.ai_logic.update_matrix()
        self.ord_matrix = []
        temp_matrix = [self.ai_logic.t[1], self.ai_logic.u[1], self.ai_logic.v[1], self.ai_logic.w[1]]
        
        # for each action, rank the reward in terms of value. Giving a matrix representing 41 states
        for i in range(4):
            count = 1
            for j in range(4):
                if i == j:
                    continue
                if temp_matrix[i] > temp_matrix[j]:
                    count += 1
            self.ord_matrix.append(count)
    
    # store ordinal values in the class to remember    
    def save_ord_matrix(self):
        self.ord_t = self.ord_matrix[0]
        self.ord_u = self.ord_matrix[1]
        self.ord_v = self.ord_matrix[2]
        self.ord_w = self.ord_matrix[3]
    
    # checks if the new calculated ordinal matrix is different to the old one, representing a change in state    
    def ord_matrix_change(self):
        if (self.ord_t != self.ord_matrix[0] or self.ord_u != self.ord_matrix[1] or self.ord_v != self.ord_matrix[2] or self.ord_w != self.ord_matrix[3]):
            self.save_ord_matrix()
            return True
        return False
    
    # updates the q matrix with new values of Q for each state change 
    def update_q_matrix(self):
        self.q_matrix = []
        self.q_matrix.append(self.q_t)
        self.q_matrix.append(self.q_u)
        self.q_matrix.append(self.q_v)
        self.q_matrix.append(self.q_w)
    
    # updates the Q value for action t.    
    def update_q_t(self):
        if self.t_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.t_count
        self.q_t = self.q_t + learning_rate*(self.ai_logic.t[1] + (self.discount * max(self.q_matrix)) - self.q_t)
    
    # updates the Q value for action u    
    def update_q_u(self):
        if self.u_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.u_count
        self.q_u = self.q_u + learning_rate*(self.ai_logic.u[1] + (self.discount * max(self.q_matrix)) - self.q_u)
    
    # updates the Q value for action v    
    def update_q_v(self):
        if self.v_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.v_count
        self.q_v = self.q_v + learning_rate*(self.ai_logic.v[1] + (self.discount * max(self.q_matrix)) - self.q_v)
    
    # updates the Q value for action w    
    def update_q_w(self):
        if self.w_count == 0:
            learning_rate = 1
        else:
            learning_rate = 1.0/self.w_count
        self.q_w = self.q_w + learning_rate*(self.ai_logic.w[1] + (self.discount * max(self.q_matrix)) - self.q_w)
    
    # updates the probability matrix after a change in Q values    
    def update_probability_matrix(self):
        self.probability_matrix = []
        self.update_q_matrix()
        total = 0
        for i in range(4):
            total += self.k ** self.q_matrix[i]
        self.probability_matrix.append((self.k**self.q_t)/total)
        self.probability_matrix.append((self.k**self.q_u)/total)
        self.probability_matrix.append((self.k**self.q_v)/total)
        self.probability_matrix.append((self.k**self.q_w)/total)
    
    # function called to inform the AI to make a move and returns the action in the form of [adult, child]    
    def move(self):
        # random number from 0 to 1
        choice = random.random()
        # determine the probablistic range of each action
        prob_t = self.probability_matrix[0]
        prob_u = self.probability_matrix[0]+self.probability_matrix[1]
        prob_v = self.probability_matrix[0]+self.probability_matrix[1]+self.probability_matrix[2]
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
        
        # find the action choice of the inner child given an adult's action choice    
        child = self.child_move(adult)
        
        if adult == "attend" and child == "go":
            self.ai_logic.attend_go()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            if self.ord_matrix_change():
                self.change += 1
                self.reset_learning_rate()
            self.t_count += 1
            self.update_q_t()
            self.update_q_matrix()
            self.update_probability_matrix()
            
        if adult == "attend" and child == "dontgo":
            self.ai_logic.attend_dontgo()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            if self.ord_matrix_change():
                self.change += 1
                self.reset_learning_rate()
            self.v_count += 1
            self.update_q_v()
            self.update_q_matrix()
            self.update_probability_matrix()
            
        if adult == "ignore" and child == "go":
            self.ai_logic.ignore_go()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            if self.ord_matrix_change():
                self.change += 1
                self.reset_learning_rate()
            self.u_count += 1
            self.update_q_u()
            self.update_q_matrix()
            self.update_probability_matrix()
                   
        if adult == "ignore" and child == "dontgo":
            self.ai_logic.ignore_dontgo()
            self.ai_logic.update_matrix()
            self.update_ord_matrix()
            if self.ord_matrix_change():
                self.change += 1
                self.reset_learning_rate()
            self.w_count += 1
            self.update_q_w()
            self.update_q_matrix()
            self.update_probability_matrix()
                
        return [adult, child]
    
    # this function prompts the child to choose an action given the adult's choice.
    # It picks the action with the greatest reward, if equal, then a random choice between go and don't go        
    def child_move(self, adult):
        if self.adult_last_move == "first":
            self.adult_last_move = adult
            child_action = random.random()
            if child_action <= 0.5:
                return "go"
            else:
                return "dontgo"

        if self.adult_last_move == "attend":
            self.adult_last_move = adult
            if self.ai_logic.t[0] > self.ai_logic.v[0]:
                return "go"
            elif self.ai_logic.t[0] < self.ai_logic.v[0]:
                return "dontgo"
            elif self.ai_logic.t[0] == self.ai_logic.v[0]:
                child_action = random.random()
                if child_action < 0.5:
                    return "go"
                else:
                    return "dontgo"
        if self.adult_last_move == "ignore":
            self.adult_last_move = adult
            if self.ai_logic.u[0] > self.ai_logic.w[0]:
                return "go"
            elif self.ai_logic.u[0] < self.ai_logic.w[0]:
                return "dontgo"
            elif self.ai_logic.u[0] == self.ai_logic.w[0]:
                child_action = random.random()
                if child_action < 0.5:
                    return "go"
                else:
                    return "dontgo"
    
    # checks if the AI won the game given an action pair    
    def check_win(self, adult, child):
        return self.ai_logic.check_win(adult, child)
    
    # returns the number of rounds the AI has played    
    def get_round(self):
        return self.ai_logic.round