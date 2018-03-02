from Chromosomes import *
from Operators import *
from Parser import *


def generateRandomChromosomes(genesize):
    genes = Chromosome()
    for i in genesize:
        genes.genes += random.randint(0,1)
    return genes
