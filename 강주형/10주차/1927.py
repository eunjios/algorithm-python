# 1927
# 최소 힙

from heapq import heappush, heappop 
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())    
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x) 