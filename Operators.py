import random
from Chromosome import Chromosome

def Crossover(parent1, parent2):
    kid1 = ""
    kid2 = ""
    for x in range(0, 4):
        kid1 += parent1.genes[x]
        kid2 += parent2.genes[x]
    for x in range(4, 8):
        kid1 += parent2.genes[x]
        kid2 += parent1.genes[x]
    newkid1 = Chromosome()
    newkid1.genes = kid1
    newkid2 = Chromosome()
    newkid2.genes = kid2
    return kid1, kid2

def Mutation(chrom):
    new = ""
    for i in range(0, chrom.genes.__len__()):
        y = random.randint(0,1)
        if y is 0:
            new += '0'
        else:
            new += '1'
    chrom.genes = new
    return chrom.genes




def main():
    '''Main'''
    p1 = Chromosome()
    p1.genes = "10101010"
    print p1.genes
    print Mutation(p1)
    

