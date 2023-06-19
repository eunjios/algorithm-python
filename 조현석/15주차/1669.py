# 멍멍이 쓰다듬기
import sys

X, Y = map(int, sys.stdin.readline().split())
diff = Y - X
count = 0
i = 1
while diff > 0:
  diff -= i
  count += 1
  if diff <= 0:
    break
  diff -= i
  count += 1
  i += 1
print(count)