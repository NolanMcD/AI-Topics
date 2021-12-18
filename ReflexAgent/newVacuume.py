import os

def betterV(stateA,stateB):
    moves = 0
    score = 0
    if stateA == 'dirty':
        print('suck')
        score += 1
        stateA = 'clean'
    if stateA == 'clean':
        print('move')
        score += 1
        moves += 1
    if stateB == 'dirty':
        print('suck')
        score += 1
        stateB = 'clean'
    if stateB == 'clean':
        print('move')
        score += 1
        moves += 1
    if moves > 1:
        print("done the score is:", score)

print('Choose one of the 4 scenarios or quit (1/2/3/4/q)')
print('1. clean, clean')
print('2. clean, dirty')
print('3. dirty, clean')
print('4. dirty, dirty')

kep = input('Choose: ')
while kep != 'q':
    if kep =='1':
        betterV('clean','clean')
    if kep == '2':
        betterV('clean','dirty')
    if kep == '3':
        betterV('dirty','clean')
    if kep == '4':
        betterV('dirty','dirty')
    kep = input('Choose: ')
    
