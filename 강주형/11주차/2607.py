# 2607
# 비슷한 단어

from collections import Counter

n = int(input())
word = Counter(input())
answer = 0

for _ in range(n-1):
    check = 0
    main_word = word
    other_word = Counter(input())
    
    # 1. 단어가 완전히 같은 경우
    if main_word == other_word:
        answer += 1
        continue
    
    # 서로 없는 문자 추가하기
    for key in main_word.keys():
        if key not in other_word.keys():
            other_word[key] = 0
    
    for key in other_word.keys():
        if key not in main_word.keys():
            main_word[key] = 0
    
    # 각 문자의 개수 비교하기
    plus, minus = 0, 0
    for key in main_word.keys():
        if abs(main_word[key] - other_word[key]) > 1:
            check = 1
            break
        elif main_word[key] - other_word[key] == 1:
            plus += 1
        elif main_word[key] - other_word[key] == -1:
            minus += 1
            
    if check == 1:
        continue
    
    # 2. 한 문자를 더하거나 뺐을 때 같은 경우
    if plus == 1 and minus == 0:
        answer += 1
    elif plus == 0 and minus == 1:
        answer += 1
    # 3. 한 문자를 다른 문자로 바꿨을 때 같은 경우
    elif plus == minus == 1:
        answer += 1

print(answer)