import sys
from collections import Counter, defaultdict

t = int(sys.stdin.readline())

for i in range(t) : 
    
    word = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    
    temp1, temp2 = float('inf'), 0 
    hashmap = Counter(word)
    
    hashmap = [i for i, v in hashmap.items() if v >= n]    
    info = defaultdict(list)
    
    for i in range(len(word)) : 
        if word[i] in hashmap :
            info[word[i]].append(i)
                        
    if not info :
        print(-1)
        continue

    for v in info.values() : 
        for j in range(len(v) - n + 1) :
            temp = v[j + n - 1] - v[j] + 1

            temp1 = min(temp, temp1)
            temp2 = max(temp, temp2)

    print(temp1, temp2)