# 21921
# 블로그

# 슬라이딩 윈도우

n, x = map(int, input().split())
visit = list(map(int, input().split()))

answer = 0

if not max(visit):
    print('SAD')
else:
    for i in range(n-x+1):
        if i == 0:
            tmp = sum(visit[:x])
            answer = tmp
            cnt = 1
        else:
            tmp += -visit[i-1] + visit[i+x-1]
            if answer == tmp:
                cnt += 1
            if answer < tmp:
                answer = tmp
                cnt = 1
    print(answer)
    print(cnt)
