def solution(n, results):
    # win[i][j] = True 이면 i가 j를 이긴다는 의미
    win = [[False] * (n+1) for _ in range(n+1)]
    
    # 직접 경기 결과 기록
    for a, b in results:
        win[a][b] = True

    # Floyd–Warshall: i->k, k->j 관계가 모두 True면 i->j도 True
    for k in range(1, n+1):
        for i in range(1, n+1):
            if win[i][k]:
                for j in range(1, n+1):
                    if win[k][j]:
                        win[i][j] = True

    answer = 0
    # 각 선수 i에 대해,
    # 나머지 n-1명 모두와의 승패 관계를 알 수 있으면 랭킹이 결정된 것
    for i in range(1, n+1):
        known = 0
        for j in range(1, n+1):
            if i == j:
                continue
            if win[i][j] or win[j][i]:
                known += 1
        if known == n - 1:
            answer += 1

    return answer
