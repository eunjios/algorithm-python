# 20006
# 랭킹전 대기열

import sys
input = sys.stdin.readline

p, n = map(int, input().split())
player = []
for _ in range(p):
    level, name = input().split()
    player.append((int(level), name))

room_number = 0
rooms = []

for i in range(p):
    if not rooms:
        rooms.append([player[i]])
    else:
        for j, room in enumerate(rooms):
            if room[0][0] - 10 <= player[i][0] <= room[0][0] + 10 and len(room) < n:
                rooms[j].append(player[i])
                break
        else:
            rooms.append([player[i]])


for room in rooms:
    
    if len(room) == n:
        print('Started!')
    else:
        print('Waiting!')
    
    for player in sorted(room, key = lambda x : x[1]):
        print(f"{player[0]} {player[1]}")