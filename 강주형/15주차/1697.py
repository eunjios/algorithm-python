# 1697
# 숨바꼭질

from collections import deque

n, k = map(int, input().split())

count = [ 1e9 for _ in range(100001) ]
visited = [ False for _ in range(100001) ]

queue = deque([n])
count[n] = 0
visited[n] = True
answer_list = []
if n == k:
    print(0)
else:
    while queue:
        now = queue.popleft()
        if now == k:
            answer_list.append(count[now])
        for next in [now+1, now-1, now*2]:
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                queue.append(next)
                count[next] = min(count[next], count[now] + 1)    
    print(min(answer_list))