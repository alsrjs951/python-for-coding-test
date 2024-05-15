#문제 : 떡볶이 떡 만들기
#파라메트릭 서치 유형의 문제
import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)
