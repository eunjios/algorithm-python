# 12919
# A와 B 2

s = input()
t = input()

min_len = len(s)
answer = 0

def recursive(t, length):
    global answer
    if length == min_len:
        if t == s:
            answer = 1 
        return None
    if t[-1] == 'A':
        recursive(t[:-1], length-1)
    if t[0] == 'B':
        recursive(t[::-1][:-1], length-1)

recursive(t, len(t))
print(answer)