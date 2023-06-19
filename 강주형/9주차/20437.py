# 문자열 게임 2
# 20437

# 슬라이딩 윈도우

from collections import defaultdict

t = int(input())

for _ in range(t):
    # alphabet_dict
    # key: alphabet, value: key에 해당하는 alphabet의 index가 담겨있는 list
    alphabet_dict = defaultdict(list)
    
    w = input()
    k = int(input())

    answer_list = []
    for idx, alphabet in enumerate(w):
        alphabet_dict[alphabet].append(idx)
        
    
    for alphabet, idx_list in alphabet_dict.items():
        for i in range(len(idx_list) - k + 1):
            # 각 알파벳의 idx_list의 idx가 k 만큼 떨어진 두 값의 차이에 1을 더한 값을 append
            # 예) idx_list = [0, 2, 3, 4, 6], k = 3 -> answer_list.extend([3 - 0 + 1, 4 - 2 + 1, 6 - 3 + 1])
            answer_list.append(idx_list[i + k - 1] - idx_list[i] + 1)

    # 만족하는 문자열이 없으면 answer_list가 empty가 되어 min, max에서 오류 발생 -> except
    try:
        print(f"{min(answer_list)} {max(answer_list)}")
    except:
        print(-1)
