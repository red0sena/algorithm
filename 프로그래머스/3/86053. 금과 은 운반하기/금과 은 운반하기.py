def solution(a, b, g, s, w, t):
    # 이분 탐색 범위 설정
    # 최악의 경우: 광물 총량 2*10^9, 무게제한 1, 편도시간 10^5
    # 왕복 2*10^5 시간이 2*10^9번 필요하므로 대략 4*10^14
    start = 0
    end = (10**9 + 10**9) * (2 * 10**5) * 2 
    answer = end

    while start <= end:
        mid = (start + end) // 2
        
        total_gold = 0    # 시간 내 운반 가능한 금의 최대 총량
        total_silver = 0  # 시간 내 운반 가능한 은의 최대 총량
        total_combined = 0 # 시간 내 운반 가능한 (금+은)의 최대 총량
        
        for i in range(len(g)):
            # 현재 시간(mid) 동안 해당 도시가 운반할 수 있는 횟수 계산
            # 왕복 시간: t[i] * 2
            # 횟수: (mid // t[i])를 하면 총 이동 횟수(편도 포함)가 나옴
            # 운반 횟수(cnt)는 (총 이동 횟수 + 1) // 2
            cnt = (mid // t[i] + 1) // 2
            
            # 해당 도시 트럭이 시간 내 나를 수 있는 최대 무게
            max_move_weight = cnt * w[i]
            
            # 1. 이 도시에서 최대로 가져올 수 있는 금 (보유량 vs 수송능력)
            total_gold += min(g[i], max_move_weight)
            
            # 2. 이 도시에서 최대로 가져올 수 있는 은 (보유량 vs 수송능력)
            total_silver += min(s[i], max_move_weight)
            
            # 3. 이 도시에서 최대로 가져올 수 있는 광물 합계 (보유총량 vs 수송능력)
            total_combined += min(g[i] + s[i], max_move_weight)
            
        # 모든 조건을 만족하는지 확인
        if total_gold >= a and total_silver >= b and total_combined >= a + b:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer