# 후보 추천하기
# heapq 에 넣을 때 (추천수, 시간(오래될수록 카운트 + 1))
from sys import stdin
input = stdin.readline

n = int(input()) # 사진 틀의 개수
k = int(input()) # 추천 횟수

students = list(map(int, input().split()))
candidates = dict() # {student: (추천수, 시간)}

for i, student in enumerate(students):
    # 후보에 있으면 추천수 하나 올림 
    if student in candidates:
        candidates[student][0] += 1
    else:
        if len(candidates) < n:
            # 새로운 후보로 올림 (추천수, 현재 시간 반영)
            candidates[student] = [1, i]
        else:
            # 추천수 적은 애 삭제
            drop = sorted(candidates.items(), key=lambda x: x[1])
            del candidates[drop[0][0]] # 해당 키로 삭제
            candidates[student] = [1, i]

candidates = map(str, sorted(candidates.keys()))
print(" ".join(candidates))

