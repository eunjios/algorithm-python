# 1446
# 지름길

# DP (or 다익스트라?)

n, d = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

# 0~d까지 index = 거리로 초기화
distance = [ i for i in range(d+1) ]

for idx in range(d+1):
    distance[idx] = min(distance[idx], distance[idx-1] + 1)
    for start, end, dist in array:
        if idx == end:
            distance[end] = min(distance[end], distance[start] + dist)

print(distance[d])
