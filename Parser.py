class Parser(object):
    
    def __init__(self, expression):
        self.expression = expression
        self.grammar = [' ', '*', '(', ')', '+']
        self.clauses = self.expression.replace('*', ' ')
        
               
def main():
    parser = Parser('(A + B) * (B + C)')
    print parser.clauses
    print parser.grammar


        
main()