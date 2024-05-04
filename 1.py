import sys

x, y = 1, 1
move_types = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

N = int(sys.stdin.readline().rstrip())
move_list = list(sys.stdin.readline().rstrip().split())

for m in move_list:
    if 1 <= x + move_types[m][0] <= N and 1 <= y + move_types[m][1] <= N:
        x += move_types[m][0]
        y += move_types[m][1]

print(x, y)