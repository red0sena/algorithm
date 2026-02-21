import sys
from collections import deque

def solve():
    # 입력 받기
    S = int(sys.stdin.readline().strip())
    
    # 최대 S는 1000이므로, 화면과 클립보드의 이모티콘 수가 2000을 넘을 필요는 없습니다.
    # (넘어갔다가 삭제하는 경우를 고려해 여유롭게 2000으로 설정)
    MAX_SIZE = 2000
    
    # dist[화면 이모티콘 수][클립보드 이모티콘 수] = 걸린 시간
    # -1로 초기화하여 방문하지 않았음을 표시
    dist = [[-1] * MAX_SIZE for _ in range(MAX_SIZE)]
    
    # BFS를 위한 큐 초기화 (초기 상태: 화면 1개, 클립보드 0개)
    queue = deque()
    queue.append((1, 0))
    dist[1][0] = 0  # 초기 상태의 시간은 0
    
    while queue:
        s, c = queue.popleft()
        
        # 목표 개수에 도달하면 걸린 시간을 반환 (BFS이므로 가장 먼저 도달한 것이 최솟값)
        if s == S:
            return dist[s][c]
        
        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        # 화면 개수(s)는 그대로, 클립보드 개수는 화면 개수(s)로 덮어쓰기
        if dist[s][s] == -1:
            dist[s][s] = dist[s][c] + 1
            queue.append((s, s))
            
        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        # 화면 개수는 (s + c), 클립보드 개수는 그대로(c)
        # 클립보드가 비어있지 않아야 하고(c > 0), 범위를 벗어나지 않아야 함
        if c > 0 and s + c < MAX_SIZE and dist[s + c][c] == -1:
            dist[s + c][c] = dist[s][c] + 1
            queue.append((s + c, c))
            
        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        # 화면 개수는 (s - 1), 클립보드 개수는 그대로(c)
        # 화면 개수가 0보다 크거나 같아야 함
        if s - 1 >= 0 and dist[s - 1][c] == -1:
            dist[s - 1][c] = dist[s][c] + 1
            queue.append((s - 1, c))

if __name__ == "__main__":
    print(solve())