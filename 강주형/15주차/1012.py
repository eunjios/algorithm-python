from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
        queue = deque([(x, y)])
        field[x][y] = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and field[nx][ny]:
                    field[nx][ny] = 0
                    queue.append((nx, ny))

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    field = [ [0] * m for _ in range(n) ]
    
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1 
        
    answer = 0

    for i in range(n):
        for j in range(m):
            if field[i][j]:
                bfs(i, j)
                answer += 1
    print(answer)