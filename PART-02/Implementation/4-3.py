# 왕실의 나이트
import sys
input = sys.stdin.readline

knight_pos = input().rstrip()

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
x = int(knight_pos[1])
y = int(ord(knight_pos[0])) - int(ord('a')) + 1

result = 0
for i in range(len(dx)):
    if 1 <= x + dx[i] <= 8 and 1 <= y + dy[i] <= 8:
        result += 1

print(result)