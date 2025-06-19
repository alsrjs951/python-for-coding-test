# 1이 될 때까지
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
count = 0

while n > 1:
    if n < k:
        count += n - 1
        break

    remainder = n % k
    if remainder == 0:
        count += 1
        n //= k
    else:
        count += remainder
        n -= remainder

print(count)
