import time
import random


NC, SC, V, TN, K, WV, G, A, M, F = [0,9,1,2,3,4,5,6,7,8]
states = [NC, SC, V, TN, K, WV, G, A, M, F]

constraints = [NC != SC, NC != V, NC != TN, NC != A, SC != G, V != WV, V != K, V != TN, TN != K, TN!= WV, TN != G, TN != A, TN != M, K != WV, G != A, G != F, A != M, A != F]

colors = ["Red", "White", "Blue", "Yellow"]

def Backtrack(states, cons, start):
    for x in range(start, len(states)):
        if cons == True:
            return states
        randy = random.randrange(4)
        if x == 1:
            mycol = states[x-1]
            if colors[randy] == mycol:
                states[x] = colors[(randy+1)%3]
            else:
                states[x] = colors[randy]
        elif x > 2:
            mycol1 = states[x-1]
            mycol2 = states[x-2]
            if colors[randy] == mycol1 or colors[randy] == mycol2:
                if colors[randy-1] == mycol1 or colors[randy-1] == mycol2:
                    states[x] = colors[randy-1]
                else:
                    states[x] = colors[randy-2]
            else:
                states[x] = colors[randy]
        else:
            states[x] = colors[randy]
        print(states)
        NC, SC, V, TN, K, WV, G, A, M, F = states
        constraints = [NC != SC, NC != V, NC != TN, NC != A, SC != G, V != WV, V != K, V != TN, TN != K, TN != WV, TN != G, TN != A, TN != M, K != WV, G != A, G != F, A != M, A != F]
        for y in constraints:
            if y == False:
#                print("Broken here")
                constraints = [NC != SC, NC != V, NC != TN, NC != A, SC != G, V != WV, V != K, V != TN, TN != K, TN != WV, TN != G, TN != A, TN != M, K != WV, G != A, G != F, A != M, A != F]
                return Backtrack(states, constraints, x)
            
start = time.time()
l = 0
while l < 5:
    states[0] = 'Red'
    Backtrack(states, constraints, 1)
    l += 1
end = time.time()
ttime = abs(start-end) / 5
print("Average time was " + str(ttime))
