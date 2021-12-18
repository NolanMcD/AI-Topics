import string
import sys
import os

def simpleVacuume(state):
    movecount = 0
    if state == 'dirty':
        print('suck')
        state = 'clean'
    if state == 'clean':
        print('move')
        movecount += 1
    if movecount > 1:
        print('agent is finished score is:', movecount)

simpleVacuume('dirty')
simpleVacuume('clean')
