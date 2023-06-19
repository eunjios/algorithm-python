import sys
from collections import deque

number = 0

def bfs(x, y) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y))
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            newx = x + row[i]
            newy = y + col[i]
            if 0 <= newx < n and 0 <= newy < n:
                if cost[newx][newy] > cost[x][y] + matrix[newx][newy]:
                    cost[newx][newy] = cost[x][y] + matrix[newx][newy]
                    queue.append((newx, newy))
        
while True :
    
    n = int(sys.stdin.readline())
    number += 1
    
    if n == 0 :
        sys.exit()
        
    matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    cost = [[float('inf')] * n for i in range(n)]
    
    cost[0][0] = matrix[0][0]
    bfs(0, 0)
    
    print(f'Problem {number}: {cost[n - 1][n - 1]}')