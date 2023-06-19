# 2531
# 회전초밥

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [ int(input()) for _ in range(n) ]


sushi_connect = sushi + sushi[:k-1]
answer = 0
for idx in range(len(sushi)):
    answer = max(answer, len(set(sushi_connect[idx:idx+k] + [c])))
        
print(answer)