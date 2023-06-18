# 유기농 배추
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        # 현재 위치 pop
        x, y = q.popleft()
        # 방문할 수 있는 곳 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖을 나가면 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 방문할 수 있으면 큐에 넣고 방문 처리 
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = -1
    return 1

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0

    # 그래프 만들기 
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        xi, yi = map(int, input().split())
        graph[yi][xi] = 1

    # 상하좌우 이동
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 그래프 순회하기 -> 방문하면 -1 로 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)