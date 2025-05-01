import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
map_list = []
for _ in range(n):
    map_list.append(list(map(int, list(input().rstrip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    map_list[x][y] = 1
    while queue:
        v = queue.popleft()
        v_x, v_y = v
        for i in range(4):
            nx = v_x + dx[i]
            ny = v_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map_list[nx][ny] == 0:
                    map_list[nx][ny] = 1
                    queue.append((nx, ny))

result = 0

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)
