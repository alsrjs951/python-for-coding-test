import sys

N = int(sys.stdin.readline().rstrip())
result = list()

for _ in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    result.append((A, int(B)))

result.sort(key=lambda x: x[1])

for student in result:
    print(student[0], end=' ')
