class Chromosome(object):

    def __init__(self):
        self.genes = ""
        self.fitness = 0

    def Fitness(self):
        num1 = int(self.genes[0]) + int(self.genes[1])
        num2 = int(self.genes[2]) + int(self.genes[3])
        num3 = int(self.genes[4]) + int(self.genes[5])
        num4 = int(self.genes[6]) + int(self.genes[7])
        self.fitness = (num1 + num2) - (num3 + num4)
        return self.fitness
            
def main():
    '''Main'''
    c = Chromosome()
    c.genes = "11001100"
    c.Fitness()
    print(c.fitness)

main()