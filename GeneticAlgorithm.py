from Chromosome import *
from Operators import *
from Parser import *
import random

def generateRandomChromosomes(genesize):
    genes = Chromosome()
    for i in range(0,genesize):
        genes.genes += str(random.randint(0,1))
    return genes

def geneticAlgorithm(data):
    parser = Parser(data)
    parser.getclauses()
    parser.getvariables()
    population = []
    
    i = 0
    for x in range(0, 6):
        population.append(generateRandomChromosomes(parser.variables.__len__()))
    while True:           
        for y in population: 
            y.SetFitness(parser)
        for c in population:
            c.SetFitnessRatio(population)
        
        population = sorted(population, key= lambda x: x.fitness_ratio, reverse= True)
        if int(population[0].fitness) is 1:
            i+=1
            print "Generation: " + str(i)
            print "Result: " + population[0].genes
            return
        p1 = population[0]
        p2 = population[1]
        i+=1
        #print str(i)+ " : " + population[0].genes + " : " + str(population[0].fitness)
        i+=1
        #print str(i)+ " : " + population[1].genes + " : " + str(population[1].fitness)
        population = []
        for n in range(0,10):
            population.append(Mutation(Crossover(p1,p2)[0]))
            population.append(Mutation(Crossover(p1,p2)[1]))

if __name__ == '__main__':
    import Main as Main
    Main.main()