import sys

N = int(sys.stdin.readline().rstrip())
result = list()

for _ in range(N):
    result.append(int(sys.stdin.readline().rstrip()))

result.sort(reverse=True)

for i in range(N):
    print(result[i], end=' ')
