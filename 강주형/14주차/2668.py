# 2668
# 숫자고르기

n = int(input())
graph = [ [] for _ in range(n+1) ]

for i in range(1, n+1):
    graph[i].append(int(input()))


def dfs(x):
    if not visited[x]:
        visited[x] = True
        for y in graph[x]:
            set1.add(x)
            set2.add(y)
        
            if set1 == set2:
                answer.extend(list(set1))
                return None
            dfs(y)
    visited[x] = False
    
    
answer = []

for i in range(1, n+1):
    visited = [False] * (n+1)
    set1, set2 = set(), set()
    dfs(i)

answer = sorted(set(answer))
print(len(answer))
for val in answer:
    print(val)