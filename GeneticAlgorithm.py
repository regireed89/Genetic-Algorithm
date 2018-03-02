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
    newpop = []
    for x in range(0, 6):
        population.append(generateRandomChromosomes(parser.variables.__len__()))
    while True:           
        for y in population: 
            y.SetFitness()
        sorted(population, key= lambda x: x.fitness, reverse= True)
        p1 = population[0]
        p2 = population[1]
        newpop = Crossover(p1,p2)
        for z in newpop:
            z.genes = Mutation(z)
        if parser.testsolution(newpop) is 1:
            print "YOLO"
            break
        else:
            population = newpop    

def main():
    p = Parser(0) 
    p.getdatafromfile("parserdata.txt")
    geneticAlgorithm(p.expression)

main()