# 16967
# 배열 복원하기

h, w, x, y = map(int, input().split())
array_b = []
for _ in range(h+x):
    array_b.append(list(map(int, input().split())))
    
array_a = [ [0] * w for _ in range(h) ]

# 리스트 슬라이싱
for i in range(h):
    for j in range(w):
        array_a[i][j] = array_b[i][j]

# 겹치는 부분 연산
for i in range(h):
    for j in range(w):
        if i >= x and j >= y:
            array_a[i][j] = array_b[i][j] - array_a[i-x][j-y]

# 출력
for i in range(h):
    for j in range(w):
        print(array_a[i][j], end=' ')
    print()