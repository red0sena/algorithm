import sys

# 표준 입력으로 여러 줄을 읽어옵니다.
input = sys.stdin.read

# 입력 데이터를 한 줄씩 처리합니다.
lines = input().strip().split('\n')

# 각 줄에 대해 A와 B를 더한 결과를 출력합니다.
for line in lines:
    A, B = map(int, line.split())
    print(A + B)
