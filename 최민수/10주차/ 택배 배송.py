import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
matrix = [[] for i in range(n + 1)]

for i in range(m) : 
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append((b, c))
    matrix[b].append((a, c))
    
def dijkstra(x) : 
    
    distance = [float('inf')] * (n + 1)
    queue = []
    
    distance[x] = 0
    heapq.heappush(queue, (0, x))
    
    while queue : 
        d, w = heapq.heappop(queue)
        for neww, newd in matrix[w] :
            
            if d + newd < distance[neww] :
                distance[neww] = d + newd
                heapq.heappush(queue, (d + newd, neww))
                
    return distance
                
result = dijkstra(1)

print(result[-1])