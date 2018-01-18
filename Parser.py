class Parser(object):
    
    def __init__(self, expression):
        self.expression = expression
        self.grammar = [' ', '*', '(', ')', '+']
        self.clauses = self.expression.replace('*', ' ')
        for e in self.expression:
            if e in self.grammar:
                self.characters = self.expression.replace(e, ' ')
            

def main():
    parser = Parser('(A + B) * (B + C)')
    print parser.clauses
    print parser.characters


        
main()