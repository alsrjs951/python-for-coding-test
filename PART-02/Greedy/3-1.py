import sys
input = sys.stdin.readline

n = int(input().rstrip())

coins = [500, 100, 50, 10]
result = 0

for coin in coins:
    result += n // coin
    n = n % coin

print(result)