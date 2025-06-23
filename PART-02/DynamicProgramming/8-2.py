# 개미 전사
import sys

input = sys.stdin.readline

n = int(input().rstrip())
input_list = list(map(int, input().rstrip().split()))

d = [0] * n
d[0] = input_list[0]
d[1] = max(d[0], input_list[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + input_list[i])

print(d[n-1])