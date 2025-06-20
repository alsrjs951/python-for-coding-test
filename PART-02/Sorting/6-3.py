# 두 배열의 원소 교체
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
a_list = list(map(int, input().rstrip().split()))
b_list = list(map(int, input().rstrip().split()))

a_list.sort()
b_list.sort(reverse=True)

for i in range(k):
    if a_list[i] < b_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
    else:
        break

print(sum(a_list))
