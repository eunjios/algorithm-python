# 1669
# 멍멍이 쓰다듬기

x, y = map(int, input().split())

num =  1

if x == y:
    print(0)
else:
    while True:
        if num**2 == y - x:
            answer = 1 + (num-1) * 2
            break
        elif num**2 > y - x:
            if y - x - (num-1)**2 < ((num) ** 2 - (num-1) ** 2) / 2:
                answer = 2 + (num-2) * 2
            else:
                answer = 3 + (num-2) * 2
            break
        num += 1
    print(answer)