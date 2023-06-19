# 정수들이 이루는 집합 -> 타고 타고 가장 여러개 연결되는 경우 구하기
# 결국 사이클인 경우를 찾아서 연결 길이를 구하는 문제 
from sys import stdin
input = stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    j = int(input())
    graph[i].append(j)
    graph[j].append(i)
visited = [False for _ in range(n+1)]

visited[1] = True
# if all(graph[i]) == 


# nums = [[i for i in range(1, n+1)]]
# [input() for _ in range(n)]
# for _ in range(n):
    