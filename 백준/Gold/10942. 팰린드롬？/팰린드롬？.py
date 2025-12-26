import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())

    # 2. DP 테이블 초기화 (0: False, 1: True)
    # dp[s][e]는 인덱스 s부터 e까지가 팰린드롬이면 1, 아니면 0
    dp = [[0] * N for _ in range(N)]

    # 3. DP 채우기
    
    # (1) 길이가 1인 경우 (무조건 팰린드롬)
    for i in range(N):
        dp[i][i] = 1
    
    # (2) 길이가 2인 경우 (두 수가 같으면 팰린드롬)
    for i in range(N - 1):
        if numbers[i] == numbers[i+1]:
            dp[i][i+1] = 1
            
    # (3) 길이가 3 이상인 경우
    # 팰린드롬 조건: 양 끝(start, end)의 값이 같고, 그 사이(start+1, end-1)가 팰린드롬이어야 함
    # length는 구간의 길이 (3부터 N까지)
    for length in range(3, N + 1):
        for start in range(N - length + 1):
            end = start + length - 1
            
            # 양 끝 숫자가 같고, 속 안의 구간이 팰린드롬인 경우
            if numbers[start] == numbers[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1

    # 4. 질문(M) 처리하기
    for _ in range(M):
        S, E = map(int, input().split())
        # 문제의 인덱스는 1부터 시작하므로 0부터 시작하도록 -1 해줌
        print(dp[S-1][E-1])

if __name__ == "__main__":
    solve()