# 9205
# 맥주 마시면서 걸어가기

from collections import deque

def bfs():
    visited_store = [ False for _ in range(n_store) ]
    
    if abs(xy_home[0] - xy_festival[0]) + abs(xy_home[1] - xy_festival[1]) <= 1000:
        return True
    
    if not n_store:
        return False
    
    queue = deque([xy_home])
    
    while queue:
        x, y = queue.popleft()
        for idx, (store_x, store_y) in enumerate(xy_store):
            if not visited_store[idx] and abs(x - store_x) + abs(y - store_y) <= 1000:
                queue.append([store_x, store_y])
                visited_store[idx] = True
        
        if abs(x-xy_festival[0]) + abs(y-xy_festival[1]) <= 1000:
            return True


t = int(input())

for _ in range(t):
    n_store = int(input())
    xy_home = list(map(int, input().split()))
    xy_store = []
    for _ in range(n_store):
        xy_store.append(list(map(int, input().split())))
    xy_festival = list(map(int, input().split()))
    
    if bfs():
        print('happy')
    else:
        print('sad')