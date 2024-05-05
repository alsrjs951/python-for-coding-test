import sys


def solution(row, col):
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
    result = 0

    for step in steps:
        if 1 <= row + step[0] <= 8 and 1 <= col + step[1] <= 8:
            result += 1
    
    return result

    
input_data = sys.stdin.readline().rstrip()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1

print(solution(row, col))
