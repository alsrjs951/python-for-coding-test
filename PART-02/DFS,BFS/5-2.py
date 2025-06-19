# 미로 탈출
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
map_list = []

for _ in range(n):
    map_list.append(list(map(int, list(input().rstrip()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    count = 1
    queue = deque([(x, y, count)])
    map_list[y][x] = 0
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                if map_list[ny][nx] == 1:
                    if nx == m - 1 and ny == n - 1:
                        return v[2] + 1
                    map_list[ny][nx] = 0
                    queue.append((nx, ny, v[2] + 1))


print(bfs(0, 0))
