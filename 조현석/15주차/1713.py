# 후보 추천하기
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
candidates = list(map(int, sys.stdin.readline().split()))

# (학생 번호, 추천 횟수, 게시된 시점)
frame = []
for i in range(M):
  # 후보가 이미 존재하는 경우
  if candidates[i] in [x[0] for x in frame]:
    for j in range(len(frame)):
      if frame[j][0] == candidates[i]:
        frame[j][1] += 1
        break
  # 후보가 존재하지 않는 경우
  else:
    # 후보가 꽉 찬 경우
    if len(frame) == N:
      # 추천 횟수가 가장 적은 후보를 제거
      frame.sort(key=lambda x: (x[1], x[2]))
      frame.pop(0)
    frame.append([candidates[i], 1, i])


frame.sort(key=lambda x: x[0])
for i in range(len(frame)):
  print(frame[i][0], end=' ')
print()