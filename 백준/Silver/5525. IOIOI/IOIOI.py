import sys
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())
S = input().rstrip()

# P_N 패턴: IOI...OI (길이 2N+1)
# S에서 P_N이 나타나는 횟수 세기
count = 0
i = 0
while i <= M - (2 * N + 1):
    # P_N은 'I'로 시작하고, 'I'와 'O'가 교대로 나타남
    if S[i] == 'I':
        valid = True
        for j in range(2 * N + 1):
            if j % 2 == 0:  # 짝수 인덱스는 'I'
                if S[i + j] != 'I':
                    valid = False
                    break
            else:  # 홀수 인덱스는 'O'
                if S[i + j] != 'O':
                    valid = False
                    break
        if valid:
            count += 1
            i += 1  # 다음 위치로 이동
        else:
            i += 1  # 패턴이 맞지 않으면 다음 위치로
    else:
        i += 1  # 'I'로 시작하지 않으면 스킵

print(count)