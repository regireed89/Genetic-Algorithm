import random
from Chromosome import Chromosome
import math
def Crossover(parent1, parent2):
    kid1 = ""
    kid2 = ""
    kids = []
    #for x in range(0, abs(parent1.genes.__len__()/2)):
     #   kid1 += parent1.genes[x]
     #   kid2 += parent2.genes[x]
    #for x in range(abs(parent1.genes.__len__()/2), parent1.genes.__len__()):
    #    kid1 += parent2.genes[x]
     #   kid2 += parent1.genes[x]
    split = math.floor(parent1.genes.__len__()/2)
    for i in range(0,parent1.genes.__len__()):
        if i < split:
            kid1 += parent1.genes[i]
            kid2 += parent2.genes[i]
        else:
            kid1 += parent2.genes[i]
            kid2 += parent1.genes[i]
    newkid1 = Chromosome()
    newkid1.genes = kid1
    newkid2 = Chromosome()
    newkid2.genes = kid2
    kids.append(newkid1)
    kids.append(newkid2)
    return kids

def Mutation(chrom):
    new = Chromosome()
    for c in chrom.genes:
        ch = c
        r = random.randint(0,100)
        if r<10:
            if c is '0':
                ch = '1'
            if c is '1':
                ch = '0'
        new.genes += ch
    return new

if __name__ == '__main__':
    import Main as Main
    Main.main()