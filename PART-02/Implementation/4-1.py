# 상하좌우
import sys
input = sys.stdin.readline

n = int(input().rstrip())
moves = input().rstrip().split()

move_type = ['L', 'R', 'U', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for move in moves:
    for i in range(len(move_type)):
        if move_type[i] == move:
            if 1 <= x + dx[i] <= n and 1 <= y + dy[i] <= n:
                x += dx[i]
                y += dy[i]
                break

print(x, y)
