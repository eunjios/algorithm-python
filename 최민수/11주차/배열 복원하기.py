import sys

h, w, x, y = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(h + x)]

for i in range(x, h) :
    for j in range(y, w) :
        matrix[i][j] -= matrix[i - x][j - y]
        
for i in range(h) : 
    print(*matrix[i][: w])