import sys

n, c = map(int, sys.stdin.readline().split())

number = [int(sys.stdin.readline()) for i in range(n)]
number.sort()

if n == 2 : 
    print(number[-1] - number[0])
    sys.exit()
    
start, end = 1, number[-1] - number[0]

result = 0

while start < end :
    
    mid = (start + end) // 2
    
    temp = number[0]
    count = 1
    
    for i in range(1, n) : 
        if number[i] - temp >= mid : 
            temp = number[i]
            count += 1
            
    if count >= c :
        result = mid
        start = mid + 1
        
    elif count < c :
        end = mid - 1
        
print(result)   
