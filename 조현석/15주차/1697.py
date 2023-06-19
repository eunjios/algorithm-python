# 숨바꼭질
import sys

M, K = map(int, sys.stdin.readline().split())

queue = [M]
visited = [0] * 100001
visited[M] = 1

while queue:
  x = queue.pop(0)
  if x == K:
    print(visited[x] - 1)
    break
  for i in (x-1, x+1, x*2):
    if 0 <= i <= 100000 and visited[i] == 0:
      visited[i] = visited[x] + 1
      queue.append(i)