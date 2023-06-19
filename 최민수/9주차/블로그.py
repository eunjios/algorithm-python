import sys 
from collections import deque

n, x = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

if sum(number) == 0 :
    print("SAD")
    sys.exit()
    
val = sum(number[ :x])

current = val
count = 1

for i in range(x, n) :
    val += (number[i] - number[i - x])
    
    if val > current :
        current = val
        count = 1
        
    elif val == current : 
        count += 1
        
print(current)
print(count)