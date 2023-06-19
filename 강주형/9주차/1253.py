# 1253
# 좋다

# 투 포인터
# comment) 처음에 sort 안 하고 풀려다가 계속 시간 초과..

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

count = 0
array.sort()

for idx, val in enumerate(array):
    start = 0
    end = n - 1
    while start < end:
        if start == idx:
            start += 1
            continue
        if end == idx:
            end -= 1
            continue
        if array[start] + array[end] < val:
            start += 1
            continue
        if array[start] + array[end] == val:
            count += 1
            break
        if array[start] + array[end] > val:
            end -= 1
    
print(count)
