# 17086
# 아기 상어 2

from collections import deque

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dist_list = []
# 대각선 포함
dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited = [ [False] * m for _ in range(n) ]
    visited[x][y] = True
    dist = [ [0] * m for _ in range(n) ]
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # array 벗어나지 않게 설정
                if array[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                
                elif array[nx][ny] == 1:

                    return dist[x][y] + 1
    return 1
    
for i in range(n):
    for j in range(m):
        if not array[i][j]:
            dist_list.append(bfs(i, j))

print(max(dist_list))