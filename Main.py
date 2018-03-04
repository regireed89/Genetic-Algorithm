from Parser import Parser
from GeneticAlgorithm import geneticAlgorithm

def main():
    '''Main'''
    p = Parser(0) 
    p.getdatafromfile("data1.txt")
    print p.expression
    print "Expected Solution: 111111111111"
    geneticAlgorithm(p.expression)
    print "\n"
    p = Parser(0) 
    p.getdatafromfile("data2.txt")
    print p.expression
    print "Expected Solution: 111111001000"
    geneticAlgorithm(p.expression)
    print "\n"
    p = Parser(0) 
    p.getdatafromfile("data3.txt")
    print p.expression
    print "Expected Solution: 00000111111111111"
    geneticAlgorithm(p.expression)
    print "\n"
    p = Parser(0) 
    p.getdatafromfile("data4.txt")
    print p.expression
    print "Expected Solution: 0101010101001"
    geneticAlgorithm(p.expression)

main()