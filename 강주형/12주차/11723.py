# 11723
# 집합

import sys
input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    input_list = list(input().split())
    if len(input_list) == 2:
        func, num = input_list[0], int(input_list[1])
    else:
        func = input_list[0]
        
    if func == 'add':
        s.add(num)
    elif func == 'remove':
        if num in s:
            s.remove(num)
    elif func == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif func == 'all':
        s = set(range(1, 21))
    elif func =='empty':
        s = set()