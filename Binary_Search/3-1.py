# 문제 : 부품 찾기
# 계수 정렬 풀이방법
import sys

n = int(sys.stdin.readline().rstrip())
array = [0] * 1000001

for i in sys.stdin.readline().rstrip().split():
    array[int(i)] = 1

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
