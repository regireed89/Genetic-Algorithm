class Chromosome(object):

    def __init__(self):
        self.genes = ""
        self.fitness = 0
        self.fitness_ratio = 0

    def SetFitness(self, cnf):
        solution = cnf.test_solution(self)
        score = 0
        for i in solution:
            if i is 1:
                score += 1
        self.fitness = float(score)/float(self.genes.__len__())

        return self.fitness
    
    def SetFitnessRatio(self,population):
        total = 0
        for c in population:
            total += c.fitness
        if float(total) < 0.001:
            return
        self.fitness_ratio = float(self.fitness)/float(total)

if __name__ == '__main__':
    import Main as Main
    Main.main()