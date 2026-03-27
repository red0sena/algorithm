import heapq
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    problems = []
    
    # 데이터를 (데드라인, 컵라면 수) 튜플로 변환
    idx = 1
    for _ in range(n):
        deadline = int(input_data[idx])
        cup_ramen = int(input_data[idx+1])
        problems.append((deadline, cup_ramen))
        idx += 2
        
    # 1. 데드라인 기준으로 오름차순 정렬
    problems.sort()
    
    pq = []
    
    for deadline, cup_ramen in problems:
        # 2. 우선순위 큐에 현재 숙제의 컵라면 수 삽입
        heapq.heappush(pq, cup_ramen)
        
        # 3. 큐의 크기가 데드라인을 초과하면 가장 작은 보상을 제거
        if len(pq) > deadline:
            heapq.heappop(pq)
            
    # 4. 남은 보상들의 총합 출력
    print(sum(pq))

if __name__ == "__main__":
    solve()