# 20922
# 겹치는 건 싫어

from collections import defaultdict

n, k = map(int, input().split())
array = list(map(int, input().split()))

answer = 0
start = 0
end = 0

num_dict = defaultdict(int)

# 기본적으로 end 전진
while end < n:
    # 현재 end(index)에서의 숫자가 k개 미만이면 계속 end 전진
    if num_dict[array[end]] < k:
        num_dict[array[end]] += 1
        end += 1
        answer = max(answer, end - start)
    # 그렇지 않으면 현재 start(index)에 있던 숫자의 빈도를 하나 빼고 (한 칸 전진하면 포함 안되니까) start 한 칸 전진
    else:
        num_dict[array[start]] -= 1
        start += 1

print(answer)