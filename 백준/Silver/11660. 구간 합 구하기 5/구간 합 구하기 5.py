import sys
input = sys.stdin.readline  # 빠른 입력을 위해 권장

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 1. 2차원 누적 합(prefix) 배열 준비
#    prefix[i][j] = (1,1)부터 (i,j)까지의 합
prefix = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = (prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1]
                        + A[i-1][j-1])

# 2. 질의 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 구간 합 = 
    # prefix[x2][y2]
    # - prefix[x2][y1-1]
    # - prefix[x1-1][y2]
    # + prefix[x1-1][y1-1]
    ans = (prefix[x2][y2]
           - prefix[x2][y1-1]
           - prefix[x1-1][y2]
           + prefix[x1-1][y1-1])
    print(ans)
