def solution(enroll, referral, seller, amount):
    # 1. 각 판매원의 부모(추천인)를 매핑하는 딕셔너리
    parent = {}
    # 2. 각 판매원의 누적 수익금을 저장하는 딕셔너리
    total_profit = {}
    
    for e, r in zip(enroll, referral):
        parent[e] = r
        total_profit[e] = 0
        
    # 3. 판매 기록을 하나씩 순회하며 수익 배분
    for s, a in zip(seller, amount):
        profit = a * 100  # 칫솔 한 개당 100원
        current = s
        
        # 추천인을 타고 올라가며 수익 분배
        while current != "-" and profit > 0:
            to_parent = profit // 10  # 추천인에게 줄 10% (원 단위 절삭)
            mine = profit - to_parent  # 내가 가질 90%
            
            # 본인 수익 누적
            total_profit[current] += mine
            
            # 다음 부모 노드로 이동 및 배분할 금액 업데이트
            current = parent[current]
            profit = to_parent

    # 4. enroll 순서에 맞게 결과 반환
    return [total_profit[name] for name in enroll]