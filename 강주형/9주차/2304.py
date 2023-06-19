# 2304
# 창고 다각형

# 구현으로 풀었는데..

n = int(input())
pillar = []
max_h = 0
for _ in range(n):
    l, h = map(int, input().split())
    pillar.append((l, h))
    max_h = max(max_h, h)
    
# l을 기준으로 오름차순 정렬
sorted_pillar = sorted(pillar, key = lambda x : x[0])

# max_h인 h의 index 저장
argmax_h = []
for idx, (l, h) in enumerate(sorted_pillar):
    if h == max_h:
        argmax_h.append(idx)
        
argmax_h_first = argmax_h[0]
argmax_h_end = argmax_h[-1]

# print(argmax_h_first,argmax_h_end)

# 필요한 기둥만 남긴 리스트
clear_pillar = []


# 첫 번째 max_h 기둥 등장 전: 앞에서부터 오름차순
for idx in range(argmax_h_first):
    # print('FIRST')
    if idx == 0:
        clear_pillar.append(sorted_pillar[idx])
        local_max_h = sorted_pillar[idx][1]
    else:
        if local_max_h < sorted_pillar[idx][1]:
            clear_pillar.append(sorted_pillar[idx])
            local_max_h = sorted_pillar[idx][1]


# max_h 기둥 한 개 넣기
clear_pillar.append(sorted_pillar[argmax_h_first])

if argmax_h_first != argmax_h_end:
    clear_pillar.append(sorted_pillar[argmax_h_end])


# 마지막 max_h 기둥 등장 후: 뒤에서부터 오름차순

tmp_pillar = []
for idx in range(len(sorted_pillar)-1, argmax_h_end, -1):
    if idx == len(sorted_pillar)-1:
        tmp_pillar.append(sorted_pillar[idx])
        local_max_h = sorted_pillar[idx][1]
    else:
        if local_max_h < sorted_pillar[idx][1]:
            tmp_pillar.append(sorted_pillar[idx])
            local_max_h = sorted_pillar[idx][1]


clear_pillar.extend(tmp_pillar[::-1])

# 직사각형에서 위에 남는 사각형들 빼기

answer = max_h * (clear_pillar[-1][0] + 1 - clear_pillar[0][0]) # 직사각형

for idx in range(1, len(clear_pillar)):
    L = clear_pillar[idx][0] - clear_pillar[idx-1][0]
    H = max_h - min(clear_pillar[idx-1][1], clear_pillar[idx][1])
    answer -= L * H
print(answer)
