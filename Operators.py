import random
from Chromosome import Chromosome

def Crossover(parent1, parent2):
    kid1 = ""
    kid2 = ""
    kids = []
    for x in range(0, abs(parent1.genes.__len__()/2)):
        kid1 += parent1.genes[x]
        kid2 += parent2.genes[x]
    for x in range(abs(parent1.genes.__len__()/2), parent1.genes.__len__()):
        kid1 += parent2.genes[x]
        kid2 += parent1.genes[x]
    newkid1 = Chromosome()
    newkid1.genes = kid1
    newkid2 = Chromosome()
    newkid2.genes = kid2
    kids.append(newkid1)
    kids.append(newkid2)
    return kids

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

