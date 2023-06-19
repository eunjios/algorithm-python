import sys

n, d = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dist = [i for i in range(d + 1)]

for i in range(d + 1) : 
    
    if i > 1 :        
        dist[i] = min(dist[i], dist[i - 1] + 1)
    
    for j, k, l in matrix :
        if i == j and k <= d :
            dist[k] = min(dist[k], dist[i] + l)
            
print(dist[d])   