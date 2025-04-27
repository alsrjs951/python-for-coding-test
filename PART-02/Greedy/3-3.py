import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

result = 0

for _ in range(n):
    row_nums = list(map(int, input().rstrip().split()))
    min_val = min(row_nums)
    result = max(result, min_val)

print(result)
