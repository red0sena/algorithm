def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    # 1. 목표 능력치 찾기
    for a_req, c_req, a_rwd, c_rwd, cost in problems:
        max_alp = max(max_alp, a_req)
        max_cop = max(max_cop, c_req)
    
    # 시작 능력이 이미 목표치보다 높을 수 있음
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # 2. DP 테이블 초기화 (무한대)
    inf = float('inf')
    dp = [[inf] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    # 3. DP 수행
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 현재 상태에서 알고력 1 올리기
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            # 현재 상태에서 코딩력 1 올리기
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            # 문제 풀기
            for a_req, c_req, a_rwd, c_rwd, cost in problems:
                if i >= a_req and j >= c_req:
                    # 목표치를 넘어가면 max_alp, max_cop에 고정
                    next_alp = min(max_alp, i + a_rwd)
                    next_cop = min(max_cop, j + c_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
    return dp[max_alp][max_cop]