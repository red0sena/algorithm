import sys
# 재귀를 사용할 경우를 대비해 한도를 늘려주지만, 여기서는 반복문으로 구현합니다.
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    # 현재 위치(x, y)와 목표 위치(r, c) 사이의 맨해튼 거리
    dist = abs(x - r) + abs(y - c)
    
    # 1. 도달 불가능한 케이스 미리 걸러내기
    # - 최소 거리보다 k가 작거나
    # - (k - 최소 거리)가 홀수면(왔다갔다를 못함) 불가능
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"
    
    answer = ""
    # 방향 우선순위: d(아래) -> l(왼쪽) -> r(오른쪽) -> u(위)
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direction = ['d', 'l', 'r', 'u']
    
    curr_x, curr_y = x, y
    
    for i in range(k):
        for j in range(4):
            nx, ny = curr_x + dx[j], curr_y + dy[j]
            
            # 격자 내부에 있고
            if 1 <= nx <= n and 1 <= ny <= m:
                # 이동 후 남은 거리 계산
                remain_dist = abs(nx - r) + abs(ny - c)
                # 남은 이동 횟수(k - 현재까지 이동한 횟수 - 1)로 도달 가능한지 확인
                if remain_dist <= (k - len(answer) - 1):
                    answer += direction[j]
                    curr_x, curr_y = nx, ny
                    break # 사전순 가장 빠른 방향을 찾았으므로 다음 k번째 이동으로
                    
    return answer