import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    days = []
    for _ in range(N):
        line = list(map(int, input().split()))
        m = line[0]
        cakes = line[1:]
        days.append(cakes)
    
    # dp[i][j] = i일에 j번 떡을 선택했을 때 가능한지
    # prev[i][j] = i일에 j를 선택했을 때, i-1일에 선택한 떡 번호
    INF = -1
    # possible[i] = i일에 선택 가능한 떡 목록
    
    # dp 방식: 각 날, 각 떡에 대해 이전 날 어떤 떡을 선택했는지 저장
    prev = [[None]*10 for _ in range(N)]  # prev[i][j] = i일에 j 선택시 i-1일 선택값
    
    # 첫째 날 초기화
    possible = [False]*10
    for c in days[0]:
        possible[c] = True
        prev[0][c] = 0  # 0은 이전 없음을 의미
    
    for i in range(1, N):
        new_possible = [False]*10
        for c in days[i]:
            # 전날 c가 아닌 떡을 선택한 경우가 있는지 확인
            for p in days[i-1]:
                if p != c and prev[i-1][p] is not None:
                    new_possible[c] = True
                    prev[i][c] = p
                    break
        possible = new_possible
    
    # 마지막 날에 선택 가능한 떡이 있는지 확인
    last_choice = None
    for c in days[N-1]:
        if prev[N-1][c] is not None:
            last_choice = c
            break
    
    if last_choice is None and N > 1:
        print(-1)
        return
    if N == 1:
        # 첫날은 무조건 가능
        print(days[0][0])
        return
    
    # 역추적
    result = [0]*N
    result[N-1] = last_choice
    for i in range(N-1, 0, -1):
        result[i-1] = prev[i][result[i]]
    
    print('\n'.join(map(str, result)))

solve()