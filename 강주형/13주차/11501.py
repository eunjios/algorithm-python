# 11501
# 주식

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    max_stock = 0
    answer = 0
    for i in range(n-1, -1, -1):
        max_stock = max(max_stock, stock[i])
        answer += max_stock - stock[i]
            
    print(answer)