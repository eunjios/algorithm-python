# 14940
# 쉬운 최단거리

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for x in range(n):
    tmp_list = list(map(int, input().split()))
    if 2 in tmp_list:
        start_x = x
        start_y = tmp_list.index(2) 
    array.append(tmp_list)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


visited = [ [False] * m for _ in range(n) ]
answer_array = [ [0] * m for _ in range(n) ]
visited[start_x][start_y] = True


def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny, n, m)
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                answer_array[nx][ny] = answer_array[x][y] + 1

bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        if array[i][j] != 0 and (start_x, start_y) != (i, j) and answer_array[i][j] == 0:
            answer_array[i][j] = -1

for i in range(n):
    for j in range(m):
        print(answer_array[i][j], end=' ')
    print()