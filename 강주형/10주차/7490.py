# 7490
# 0 만들기

t = int(input())

def recursive(string, m):
    if len(string) == m:
        operators.append(string+' ')
        return
    
    string += ' '
    recursive(string, n-1)
    string = string[:-1]
    
    string += '+'
    recursive(string, n-1)
    string = string[:-1]
        
    string += '-'
    recursive(string, n-1)
    string = string[:-1]
    
for _ in range(t):
    n = int(input())
    
    operators = []
    recursive('', n-1)
    for operator in operators:
        expression = ''
        for opr, num in zip(operator, range(1, n+1)):
            expression += str(num) + opr
        
        if eval(expression.replace(' ', '')) == 0:
            print(expression)
    print()