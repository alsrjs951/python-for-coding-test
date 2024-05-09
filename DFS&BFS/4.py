import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [[] for _ in range(N)]

for i in range(N):
    maze[i] = list(map(int, list(sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, start):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x + dx[i] >= 0 and x + dx[i] < N and y + dy[i] >= 0 and y + dy[i] < M:
                if graph[x+dx[i]][y+dy[i]] == 1:
                    queue.append((x+dx[i], y+dy[i]))
                    graph[x+dx[i]][y+dy[i]] = graph[x][y] + 1
    
    return graph[N-1][M-1]

print(bfs(maze, (0, 0)))
