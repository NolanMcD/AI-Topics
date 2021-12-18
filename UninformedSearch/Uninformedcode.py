#by Nolan McDermott
import os
import time

actions = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]

def nodecheck(node):
    if node[0] > 3 or node[1] > 3:
        return False
    elif node[0] < 0 or node[1] < 0:
        return False
    elif node[0] == 2 and node[1] == 1:
        return False
    elif node[0] == 1 and node[1] == 0:
        return False
    elif node[0] == 1 and node[1] == 3:
        return False
    elif node[0] == 1 and node[1] == 2:
        return False
    elif node[0] == 2 and node[1] == 3:
        return False
    else:
        return True

def interativeDeep():
    for i in range(25):
        s = depthlimited(i)
        if s == [0,0,0]:
            print("Done at level " + str(i))
            break


def depthlimited(limit):
    node = [3,3,1]
    solution = recursiveDLS(node, limit, 1)
    return solution


beenhere = []

def recursiveDLS(node, limit, level):
    print("Node is: ")
    print(node)
    beenhere.append(node)
    if node == [0,0,0]:
        print(node)
        print("Done! at level " + str(level))
        return node
    elif limit == 0:
        print("Limit reached")
        return node
    else:
        for i in range(len(actions)):
            if node[2] == 1:
                child = [node[0] - actions[i][0], node[1] - actions[i][1], node[2] - actions[i][2]]
            else:
                child = [node[0] + actions[i][0], node[1] + actions[i][1], node[2] + actions[i][2]]
            if child in beenhere:
                continue
            elif nodecheck(child) == True:
                result = recursiveDLS(child, limit - 1, level + 1)

recursiveDLS([3,3,1],25,1)

