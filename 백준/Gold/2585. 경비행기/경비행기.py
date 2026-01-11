import sys
import math
from collections import deque

# 빠른 입력을 위해 sys.stdin 사용
input = sys.stdin.readline

def solve():
    # 입력 받기
    # n: 비행장 개수, k: 최대 경유 가능 횟수
    n, k = map(int, input().split())
    
    # 좌표 리스트: [출발지] + [중간 비행장들] + [도착지]
    # 출발지: (0, 0), 도착지: (10000, 10000)
    coords = []
    coords.append((0, 0))
    for _ in range(n):
        coords.append(tuple(map(int, input().split())))
    coords.append((10000, 10000))

    # 두 지점 사이의 필요 연료 계산 함수
    def get_fuel(p1, p2):
        dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        # 10km당 1리터, 소수점 올림 처리
        return math.ceil(dist / 10)

    # 결정 문제: 용량이 limit일 때 k번 이하 경유로 도착 가능한가?
    def can_reach(limit):
        # q: (현재 위치 인덱스, 현재까지 경유 횟수)
        q = deque([(0, 0)])
        visited = [False] * (n + 2)
        visited[0] = True
        
        while q:
            curr_idx, stop_count = q.popleft()
            
            # 현재 위치에서 갈 수 있는 모든 노드 탐색
            for next_idx in range(n + 2):
                if curr_idx == next_idx: continue
                
                # 목적지(n+1번 인덱스)에 도달 가능한 경우
                if next_idx == n + 1:
                    if get_fuel(coords[curr_idx], coords[next_idx]) <= limit:
                        return True
                    continue
                
                # 아직 방문하지 않았고, 경유 횟수가 남았으며, 연료통 용량으로 갈 수 있는 경우
                if not visited[next_idx] and stop_count < k:
                    if get_fuel(coords[curr_idx], coords[next_idx]) <= limit:
                        visited[next_idx] = True
                        q.append((next_idx, stop_count + 1))
        
        return False

    # 이분 탐색 (Binary Search)
    # 최소 연료 1, 최대 연료는 대략 1500 (10000, 10000까지 직통 시 약 1415)
    low, high = 1, 1500
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if can_reach(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    solve()