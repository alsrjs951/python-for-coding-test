# 효율적인 화폐 구성
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
money = list()
for _ in range(n):
    money.append(int(input().rstrip()))

d = [10001] * 10001

for i in money:
    d[i] = 1

for i in money:
    for j in range(i, m+1, i):
        d[j] = min(d[j-i] + 1, d[j])

if d[m] > 10000:
    print(-1)
else:
    print(d[m])
