# 위에서 아래로
import sys

input = sys.stdin.readline

num_list = []

n = int(input().rstrip())
for _ in range(n):
    num_list.append(int(input().rstrip()))

for num in sorted(num_list, reverse=True):
    print(num, end=' ')