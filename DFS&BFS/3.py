import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(N):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      result += 1

print(result)
