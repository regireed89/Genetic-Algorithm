class Parser(object):
    
    def __init__(self, expression):
        self.expression = expression
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~']
        self.clauseAmt = 0
        self.storage = []
        self.variables = []

    def getdatafromfile(self, filename):
        dafile = open(filename, 'ab+')
        self.expression = dafile.read()

    def getclauseamt(self):
        self.clauseAmt = 0
        for e in self.expression:
            if e is '(':
                self.clauseAmt += 1
        return 'Clause Amount' + str(self.clauseAmt)
                   
    def getvariables(self):
        test = []
        self.variables = self.expression
        for i in self.grammar:
            self.variables = self.variables.replace(i,'')
        for d in self.variables:
            if d not in test:
                test.append(d)
        self.variables = sorted(test, key=lambda x: x)
        return self.variables
        
    def getclauses(self):
        self.storage = []
        copy = False
        addstring = ""
        for x in self.expression:
            if x is '(':
                copy = True
            if copy:
                addstring += x
            if x is ')':
                copy = False
                self.storage.append(addstring)
                addstring = ""
        return self.storage

    def Change(self):
        new = ""
        for x in self.storage:
            for c in x:
                if c is '+':
                    new += '|'
                elif c is '*':
                    new += '^'
                elif c is '!':
                    new  += '~'
                else:
                    new += c
        self.expression = new 
        self.getvariables()
        self.getclauses()
        self.getclauseamt()

    def test_solution(self, solution):
        result = []
        variables = {}
        self.Change()
        i = 0
        for v in self.variables:
            variables[v] = solution.genes[i]
            i += 1
        clauses = self.storage
        for c in clauses:
            clauseval = ''
            for place in range(1, str(c).__len__()-1):
                if c[place] in self.variables:
                    clauseval += variables[c[place]]
                else:
                    clauseval += c[place]
            result.append(eval(clauseval))    
        fixedResult = []
        for r in result:
            if r is -1:
                fixedResult.append(1)
            elif r is -2:
                fixedResult.append(0)
            else:
                fixedResult.append(r)
        return fixedResult    

if __name__ == '__main__':
    import Main as Main
    Main.main()