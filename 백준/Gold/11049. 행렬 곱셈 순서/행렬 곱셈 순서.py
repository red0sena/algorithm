import sys

def solve():
    N = int(sys.stdin.readline())
    matrices = []
    for _ in range(N):
        matrices.append(list(map(int, sys.stdin.readline().split())))

    # DP 테이블 초기화
    # dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱하는 데 필요한 최소 연산 횟수
    dp = [[0] * N for _ in range(N)]

    # len: 곱하는 행렬의 개수 (체인의 길이)
    for length in range(1, N):
        # i: 시작 행렬의 인덱스
        for i in range(N - length):
            # j: 끝 행렬의 인덱스
            j = i + length
            
            # dp[i][j]를 큰 값으로 초기화
            dp[i][j] = float('inf')
            
            # k: 분할 지점
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                if dp[i][j] > cost:
                    dp[i][j] = cost

    print(dp[0][N-1])

solve()