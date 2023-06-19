# 19941
# 햄버거 분배

n, k = map(int, input().split())
s = list(input())

count = 0

for i in range(len(s)):
    if s[i] == 'P':
        start = max(0, i-k)
        end = min(n, i+k+1)
        for j in range(start, end):
            if s[j] == 'H':
                s[j] = 'X'
                count += 1
                break
print(count)