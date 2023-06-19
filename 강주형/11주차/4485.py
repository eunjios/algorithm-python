import heapq
import sys
input = sys.stdin.readline
count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    cave = []
    for _ in range(n):
        cave.append(list(map(int, input().split())))

    graph = [ [[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i > 0:
                graph[i][j].append(((i-1, j), cave[i-1][j]))
                graph[i-1][j].append(((i, j), cave[i][j]))
            if j > 0:
                graph[i][j].append(((i, j-1), cave[i][j-1]))
                graph[i][j-1].append(((i, j), cave[i][j]))
                
    INF = 1e9

    def dijkstra(x, y):
        q = []
        heapq.heappush(q, (cave[x][y], (x, y)))
        distance[x][y] = cave[x][y]
        while q:
            dist, now = heapq.heappop(q)
            x, y = now
            if distance[x][y] < dist:
                continue
            for i in graph[x][y]:
                cost = dist + i[1]
                if cost < distance[i[0][0]][i[0][1]]:
                    distance[i[0][0]][i[0][1]] = cost
                    heapq.heappush(q, (cost, i[0]))

    distance = [ [ INF for _ in range(n)] for _ in range(n)]

    dijkstra(0, 0)

    print(f"Problem {count}: {distance[n-1][n-1]}")