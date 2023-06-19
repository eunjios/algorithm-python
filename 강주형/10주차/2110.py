# 2110
# 공유기 설치

# Binary Search
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

def binary_search(array, start, end):
    answer = 0
    max_diff = end
    while start <= end:
        install = 1
        now = array[0]
        mid = (start + end) // 2
        diff = max_diff
        for i in range(1, n):
            if array[i] - now >= mid:
                diff = min(diff, array[i] - now)
                install += 1
                now = array[i]
        if install >= c:
            start = mid + 1
            answer = max(answer, diff)                
        else:
            end = mid - 1
    return answer

start = 1
end = array[-1] - array[0] 

print(binary_search(array, start, end))
