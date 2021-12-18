#class that implements the MiniMax algorithm.
import random
import sys
import math
import Square
from TicTacToeAction import TicTacToeAction

class AlphaBetaSearch:
    def __init__(self):
        self.numberOfStates=0 #< counter to measure the number of iterations / states.

    # Start procedure of the MiniMax algorithm.
    # state: The state where the MiniMax algorithm starts searching
    # usePruning: Whether to use alpha - beta - pruning
    # return An optimal action to be taken at this point.
    def AlphaBetaDecision(self,state):
        self.numberOfStates = 0
        actions = state.getActions()
        utility=[]
        alpha=-1
        beta=1
        for action in actions:
            scores=[]
            s=state.getResult(action)
            utility.append(self.MinValue(s,alpha,beta))
            s.restoreState(action)
        for i in range(len(actions)):
            if utility[i] == max(utility):
                action = actions[i]
                break
        print("State space size: " , self.numberOfStates)
        return action

        
    def MaxValue(self,state,alpha,beta):
        self.numberOfStates+=1
        if state.isTerminal():
            return state.getUtility()
        v=-10000
        actions = state.getActions()
        utility=[]
        for action in actions:
            scores=[]
            s=state.getResult(action)
            utility.append(self.MinValue(s,alpha,beta))
            s.restoreState(action)
            v=max(utility)
            if v == beta:
                return v
        v=max(utility)
        return v
    
       
    def MinValue(self, state, alpha, beta):
        self.numberOfStates += 1
        if state.isTerminal():
            return state.getUtility()
        v=10000
        actions = state.getActions()
        utility=[]
        for action in actions:
            scores=[]
            s=state.getResult(action)
            utility.append(self.MaxValue(s,alpha,beta))
            s.restoreState(action)
            v=min(utility)
            if v == alpha:
                return v
        v=min(utility)
        return v

