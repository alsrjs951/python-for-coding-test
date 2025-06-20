# 성적이 낮은 순서로 학생 출력하기
import sys

input = sys.stdin.readline

student_info = []

n = int(input())
for _ in range(n):
    name, score = input().rstrip().split()
    student_info.append((name, score))

for info in sorted(student_info, key=lambda x: x[1]):
    print(info[0], end=' ')