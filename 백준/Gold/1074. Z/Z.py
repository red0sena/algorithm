
import sys
input_data = sys.stdin.readline().strip().split()
N, r, c = map(int, input_data)

answer = 0
# N번만큼(배열 크기가 2^N이 될 때까지) 반복
for i in range(N):
    # 현재 절반 크기 (2^(N-1-i))
    half = 1 << (N - 1 - i)  # 2^(N-1-i)

    # 현재 좌표 (r, c)가 어느 사분면에 속하는지 판단
    rowQuad = 1 if r >= half else 0
    colQuad = 1 if c >= half else 0

    # 사분면(0,1,2,3)에 따라 offset 계산
    quad = 2 * rowQuad + colQuad

    # 한 사분면에 있는 원소 개수 = 2^(2*(N-1-i))
    answer += quad * (1 << (2 * (N - 1 - i)))

    # 해당 사분면 내부 좌표로 (r, c) 업데이트
    if rowQuad == 1:
        r -= half
    if colQuad == 1:
        c -= half

print(answer)


