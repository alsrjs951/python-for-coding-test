# 부품 찾기
import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input().rstrip())
n_list = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
m_list = list(map(int, input().rstrip().split()))

for target in m_list:
    if binary_search(n_list, target, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')