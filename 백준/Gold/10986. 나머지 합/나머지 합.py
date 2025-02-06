import sys
input_data = sys.stdin.read().strip().split()

# 1. 입력 받기
N, M = map(int, input_data[:2])
A = list(map(int, input_data[2:]))

# 2. 누적합 배열(prefix sum mod M) 계산
prefix_mod = [0] * (N+1)  # S_0 = 0 포함
for i in range(1, N+1):
    prefix_mod[i] = (prefix_mod[i-1] + A[i-1]) % M

# 3. 나머지별 빈도수 계산
count = [0] * M
for pm in prefix_mod:
    count[pm] += 1

        # 4. 같은 나머지를 갖는 인덱스 쌍 세기
answer = 0
for r in range(M):
    if count[r] > 1:
        answer += count[r] * (count[r] - 1) // 2

print(answer)