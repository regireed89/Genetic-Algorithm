class Chromosome(object):

    def __init__(self):
        self.genes = ""
        self.fitness = 0

    def SetFitness(self):
        for i in self.genes:
            if i is '1':
                self.fitness += 1
        return self.fitness