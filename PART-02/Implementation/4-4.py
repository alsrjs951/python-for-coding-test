import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
x, y, d = map(int, input().rstrip().split())
map_data = list()
for _ in range(n):
    map_data.append(list(map(int, input().rstrip().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

while True:
    flag = 0
    for _ in range(len(dx)):
        if d == 0:
            d = 3
        else:
            d -= 1
        nx = x + dx[d]
        ny = y + dy[d]
        if map_data[nx][ny] == 1:
            continue
        x = nx
        y = ny
        map_data[x][y] = 1
        flag = 1
        break
    
    if flag == 1:
        result += 1
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if map_data[nx][ny] == 1:
            break
        x = nx
        y = ny

print(result)
