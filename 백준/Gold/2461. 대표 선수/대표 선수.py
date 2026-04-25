import heapq
import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    N = int(input[0])  # 학급 수
    M = int(input[1])  # 학생 수
    
    classes = []
    idx = 2
    for _ in range(N):
        # 각 학급의 점수를 정렬하여 저장
        row = sorted(map(int, input[idx:idx+M]))
        classes.append(row)
        idx += M
    
    pq = []
    current_max = 0
    
    # 1. 초기 설정: 각 학급의 첫 번째(가장 작은) 학생들을 큐에 삽입
    for i in range(N):
        # (능력치, 학급 인덱스, 학생 인덱스)
        heapq.heappush(pq, (classes[i][0], i, 0))
        current_max = max(current_max, classes[i][0])
    
    min_diff = float('inf')
    
    # 2. 우선순위 큐를 이용한 탐색
    while pq:
        current_min, class_idx, student_idx = heapq.heappop(pq)
        
        # 최댓값과 최솟값의 차이 갱신
        min_diff = min(min_diff, current_max - current_min)
        
        # 해당 학급에 다음 학생이 남아있다면 큐에 추가
        if student_idx + 1 < M:
            next_val = classes[class_idx][student_idx + 1]
            heapq.heappush(pq, (next_val, class_idx, student_idx + 1))
            # 새로 들어온 학생이 현재 팀의 최댓값보다 크면 갱신
            current_max = max(current_max, next_val)
        else:
            # 한 학급이라도 모든 학생을 검사했다면 종료
            break
            
    print(min_diff)

if __name__ == "__main__":
    solve()