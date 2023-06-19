import sys

n = int(sys.stdin.readline())
target = list(sys.stdin.readline().rstrip())

count = 0

for i in range(n - 1) :
    
    word = list(sys.stdin.readline().rstrip())
    temp = target[:]
    
    if len(word) == len(temp) :
        for j in word :
            if j in temp :
                temp.remove(j)
       
        if len(temp) == 0 or len(temp) == 1 :
            count += 1
           
        
    elif len(word) - len(temp) == 1 :
        for j in temp :
            if j in word :
                word.remove(j)
                
        if len(word) == 1 :
            count += 1
            
    elif len(temp) - len(word) == 1 :
        for j in word :
            if j in temp :
                temp.remove(j)
                
        if len(temp) == 1 :
            count += 1
            
print(count)