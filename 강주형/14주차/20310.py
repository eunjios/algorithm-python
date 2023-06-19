# 20310
# 타노스

s = list(input())

count_0 = s.count('0')
count_1 = s.count('1')

for _ in range(count_1 // 2):
    s.remove('1')

s = s[::-1]

for _ in range(count_0 // 2):
    s.remove('0')
    
print(''.join(s[::-1]))