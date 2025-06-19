# 큰 수의 법칙
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))

max_number = numbers[n-1]
second_max_number = numbers[n-2]

max_number_count = m // (k+1) * k

result = max_number_count * max_number + (m - max_number_count) * second_max_number

print(result)
