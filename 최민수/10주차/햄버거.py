import sys

n, k = map(int, sys.stdin.readline().split())
word = list(sys.stdin.readline().rstrip())

idx = [i for i in range(len(word)) if word[i] == 'P']

count = 0

for i in idx :
    start, end = i - k, i + k
    
    if start < 0 :
        start = 0
        
    if end > len(word) - 1 :
        end = len(word) - 1
        
    for j in range(start, end + 1) : 
        if word[j] == 'H' :
            count += 1 
            word[j] = 'E'
            break
            
print(count)