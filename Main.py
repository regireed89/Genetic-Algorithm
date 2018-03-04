from Parser import Parser
from GeneticAlgorithm import geneticAlgorithm

def main():
    '''Main'''
    p = Parser(0) 
    p.getdatafromfile("parserdata.txt")
    geneticAlgorithm(p.expression)

main()