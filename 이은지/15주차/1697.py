from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == k: # 동생 위치면 
            return time[x] # 걸린시간 return 
        for nx in [x-1, x+1, 2*x]:
            # 범위 벗어나면
            if nx < 0 or nx > 100000:
                continue
            # 방문한 적 없으면
            if time[nx] == 0:
                time[nx] = time[x] + 1
                q.append(nx)

n, k = map(int, input().split()) # 수빈 위치, 동생 위치
time = [0 for _ in range(100001)] # 걸린 시간 (처음엔 0, 거쳐온 경로 저장)
print(bfs(n))