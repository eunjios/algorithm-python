# 1238
# 파티

# 다익스트라 알고리즘
# 이코테 다익스트라 알고리즘 참고 및 변형
# heap 사용하지 않은 다익스트라 -> 시간초과
# 다익스트라 함수가 어떻게 돌아가는 건지 다시 공부해야 됨..

import sys
import heapq

input = sys.stdin.readline

INF  = int(1e9) #무한을 의미하는 값으로 10억 설정

#노드의 개수, 간선의 개수, 목적지를 입력받기
n, m, x = map(int,input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

#모든 간선 정보를 입력받기:
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미.
    graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드의 번호를 반환
    for i in range(1,n+1):
      if distance[i] < min_value and not visited[i]:
        min_value = distance[i]
        index = i
    return index

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

go = [ i for i in range(n+1) ]
for i in range(1, n+1):
    #방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    visited = [False] * (n+1)
    #최단거리 테이블을 모두 무한으로 초기화
    distance =[INF] * (n+1)
    #다익스트라 알고리즘 수행
    dijkstra(i)  
    if i == x:
        back = distance.copy()
    else:
        go[i] = distance[x]

# 자기자신 제거
del go[x]
del back[x]

print(max([go[i] + back[i] for i in range(1, len(go))]))
