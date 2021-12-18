#class that implements the MiniMax algorithm.
import random
import sys
import math
import Square
from TicTacToeAction import TicTacToeAction
from AlphaBetaSearch import AlphaBetaSearch


class MiniMax:
    def __init__(self):
        self.numberOfStates=0 #< counter to measure the number of iterations / states.
        self.usePruning=False

    def MinimaxDecision(self,state, usePruning):
        self.usePruning = usePruning
        if usePruning:
            alphaBeta = AlphaBetaSearch()
            action = alphaBeta.AlphaBetaDecision(state)
            return action
        self.numberOfStates = 0
        actions = state.getActions()
        utility=[]
        for action in actions:
            scores=[]
            s=state.getResult(action)
            
            utility.append(self.MinValue(s))
            s.restoreState(action)
        for i in range(len(actions)):
            if utility[i] == max(utility):
                action = actions[i]
                break
        print("State space size: " , self.numberOfStates)
        return action

    def MaxValue(self,state):
        self.numberOfStates+=1
        if state.isTerminal():
            return state.getUtility()
        v=-10000
        actions = state.getActions()
        utility=[]
        for action in actions:
            scores=[]
            s=state.getResult(action)
            utility.append(self.MinValue(s))
            s.restoreState(action)
        v=max(utility)
        return v

    def MinValue(self, state):
        self.numberOfStates += 1
        if state.isTerminal():
            return state.getUtility()
        v=10000
        actions = state.getActions()
        utility=[]
        for action in actions:
            s=state.getResult(action)
            utility.append(self.MaxValue(s))
            s.restoreState(action)
        v=min(utility)
        return v

