from Chromosome import *
from Operators import *
from Parser import *


def generateRandomChromosomes(genesize):
    genes = Chromosome()
    for i in range(0,genesize):
        genes.genes += str(random.randint(0,1))
    return genes.genes

def geneticAlgorithm():
    population = []
   

def main():
    print generateRandomChromosomes(9)

