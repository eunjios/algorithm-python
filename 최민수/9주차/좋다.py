import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

number.sort()
count = 0

for i in range(n) :
    temp = number[: i] + number[i + 1 :]
    left, right = 0, n - 2
    
    print(right)

    while left < right : 
        ans = temp[left] + temp[right]
        
        if ans == number[i] :
            count += 1
            break
            
        elif ans < number[i] :
            left += 1
            
        else : 
            right -= 1
            
print(count)