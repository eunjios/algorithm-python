import sys

t = int(sys.stdin.readline())

result = []
operator = [' ', '+', '-']

def cal(x) :
    
    form = x.replace(' ', '')
    
    if eval(form) == 0 :
        result.append(x)
        
def solve(now, number) : 
    
    if now == n + 1 : 
        cal(number)
        return
    
    for i in operator : 
        solve(now + 1, number + i + str(now))

for i in range(t) :
    n = int(sys.stdin.readline())
    solve(2, '1')
    result.append(' ')
    
for i in result : 
    print(i)