#! /usr/bin/env python3

import vector2D
import environment
import math

def greedySearch(env):
    #
    # TODO: return a path from start to goal using greedy search
        #
    return []

def uniformCostSearch(env):
            #
            # TODO
            #
    return []


def astarSearch(env):
    path = []
    path.append(env.start)
    astar = []
    for a in env.obstacles:
        for b in a.vertices:
            SLD = math.sqrt( (env.width - b.x)**2 + (env.height - b.y)**2)
            DIS = math.sqrt( (env.start.x - b.x)**2 + ( env.start.y - b.y)**2)
            ASTAR = SLD + DIS
            astar.append(ASTAR)
            if ASTAR == min(astar):
                path.append(b)
                env.start = vector2D.Vector2D(b.x, b.y)
                
    path.append(vector2D.Vector2D(env.width,env.height))
    return path

if __name__ == '__main__':
    env = environment.Environment('output/environment.txt')
    print("Loaded an environment with {} obstacles.".format(len(env.obstacles)))

    searches = {
        'greedy': greedySearch,
                        'uniformcost': uniformCostSearch,
                        'astar': astarSearch
                    }

    for name, fun in searches.items():
        print("Attempting a search with " + name)
        environment.printPath(name, fun(env))
                            
