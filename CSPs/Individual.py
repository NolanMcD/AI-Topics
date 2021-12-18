import random
# Author Fan Zhang
class Individual:
	# Updates the fitness value based on the genom and the map.
    def updateFitness(self,map,genome):
        #TODO implement fitness function
        colors = ['Red','White','Blue','Yellow']
        conflict = 0
        x = 0
        mut = 0
        for i in range(len(map.borders)):
            #print(map.borders[i].index1, map.borders[i].index2)
            if genome[map.borders[i].index1] == genome[map.borders[i].index2]:
                conflict += 1
                mut = i
        if conflict == 0:
            print("Solution Found!")
            exit
        elif conflict > 2:
            print("fitness too high, run abandoned")
            ## trying to make it better
            x += 1
            if x > 1000:
                print("Soltuion not found in 1000 interations")
                exit
            print("Starting new run")
            genno = []
            for l in range(len(map.borders)):
                dandy = random.randrange(4)
                genno.append(colors[dandy])
            self.updateFitness(map,genno)
        elif conflict <= 2 and conflict > 0:
            print("Mutating")
            x += 1
            if x > 500:
                print("Solution not found in 500 iterations")
            landy = random.randrange(4)
            genome[map.borders[mut].index1] = colors[landy]
            print("New Genome is: ", genome)
            self.updateFitness(map,genome)
        print(conflict)
        self.fitness=conflict

    def __init__(self,map):
        self.map=map# the map
        
        #print(map.states)
        #print(map.borders[0].index1)
        #print(map.borders[1].index2)
        bigG = []
        for i in map.states:
            colors = ['Red','White','Blue','Yellow']
            randy = random.randrange(4)
            color = colors[randy]
            print(i + ": " + color)
            genome = color
            bigG.append(genome)
        self.fitness=0# fitness is cached and only updated on request whenever necessary
        # TODO some representation of the genom of the individual
        # TODO implement random generation of an individual
        
        self.updateFitness(map,bigG)

    # Reproduces a child randomly from two individuals (see textbook).
	# x The first parent.
	# y The second parent.
	# return The child created from the two individuals.
    def reproduce(self,x, y):
        #child = Individual(x.map)
        child = Individual(x)
        # TODO reproduce child from individuals x and y
        child.updateFitness()
        return child

	# Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        self.updateFitness()

	# Checks whether the individual represents a valid goal state.
	# return Whether the individual represents a valid goal state.
    def isGoal(self):
        #return self.fitness == len(self.map.border)
        return 0

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...

