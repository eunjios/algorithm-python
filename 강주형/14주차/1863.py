# 1863
# 스카이라인 쉬운거

import sys

input = sys.stdin.readline

n = int(input())

array = []
answer = 0
for _ in range(n):
    # y: 끝나는 지점
    x, y = map(int, input().split())
    array.append(y)
    
# 마지막엔 항상 0으로 끝남
array.append(0)

stack = [0]

for val in array:
    height = val
    # while: 높이가 낮아질 때
    while stack[-1] > val:
        # 높이가 낮아질 때, 건물이 하나 초과해서 끝날 수 있으므로 height를 업데이트 하면서 개수 세기
        if stack[-1] != height:
            answer += 1
            height = stack[-1]
        
        # 다음 번 돌 때 stack[-1]이 앞에 꺼로 업데이트 됨
        stack.pop()
    stack.append(val)
print(answer)