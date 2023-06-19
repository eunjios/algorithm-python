import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

shark = deque()

for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1 :
            shark.append((i, j))
            
def bfs(queue) :
    
    row = [1, 1, 1, 0, 0, -1, -1, -1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    while queue : 
        x, y = queue.popleft()
        for i in range(8) :
            newx = x + row[i]
            newy = y + col[i]
            if 0 <= newx < n and 0 <= newy < m :
                if matrix[newx][newy] == 0 :
                    matrix[newx][newy] = matrix[x][y] + 1
                    queue.append((newx, newy))
                                      
bfs(shark)

result = 0

for i in range(n):
    for j in range(m):
        result = max(result, matrix[i][j])

print(result - 1)