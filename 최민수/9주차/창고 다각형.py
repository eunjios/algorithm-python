import sys

n = int(sys.stdin.readline())

number = []

idx = 0
max_height = 0

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    
    if b > max_height : 
        max_height = b
    
    number.append((a, b))
    
number.sort()
result = max_height

for i in range(n) :
    if number[i][1] == max_height :
        idx = i

left = number[0][1]

for i in range(idx) :
    
    result += left * (number[i+1][0] - number[i][0]) 
    left = max(left, number[i+1][1])
    
right = number[-1][1]

for i in range(n - 1, idx, -1) : 
    
    result += right * (number[i][0] - number[i-1][0]) 
    right = max(right, number[i-1][1])
    
print(result)    